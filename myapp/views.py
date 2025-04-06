import os
import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime
from django.contrib import messages
from .forms import CustomUserCreationForm, LagerForm, ArtikelForm
from .models import User, Lager, Artikel, Transaction


# 1. Benutzerregistrierung
def register(request):
    """Registrierung eines neuen Benutzers und automatisches Login."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Dieser Benutzername ist bereits vergeben.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Diese E-Mail-Adresse ist bereits registriert.')
            else:
                user = form.save()
                login(request, user)
                messages.success(request, 'Registrierung erfolgreich! Du bist nun eingeloggt.')
                return redirect('lager_list')
        else:
            messages.error(request, 'Bitte korrigiere die Fehler im Formular.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


# 2. Lagerverwaltung
@login_required
def lager_create(request):
    """Erstellt ein neues Lager und ordnet es dem Benutzer zu."""
    form = LagerForm(request.POST or None)
    if form.is_valid():
        lager = form.save(commit=False)
        lager.owner = request.user
        lager.save()
        lager.users.add(request.user)
        messages.success(request, 'Lager wurde erfolgreich erstellt!')
        return redirect('lager_list')
    return render(request, 'lager_form.html', {'form': form})


@login_required
def lager_list(request):
    """Zeigt die Liste der Lager des angemeldeten Benutzers."""
    lager = Lager.objects.filter(users=request.user)
    if not lager.exists():
        messages.info(request, 'Du hast noch keine Lager angelegt.')
    return render(request, 'lager_list.html', {'lager': lager})


# 3. Artikelverwaltung
@login_required
def artikel_create(request, lager_id):
    """Fügt einen neuen Artikel hinzu."""
    lager = get_object_or_404(Lager, id=lager_id)
    form = ArtikelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artikel_name = form.cleaned_data['name']
        if Artikel.objects.filter(lager=lager, name=artikel_name).exists():
            messages.error(request, 'Dieser Artikel existiert bereits im Lager!')
        else:
            artikel = form.save(commit=False)
            artikel.lager = lager
            artikel.save()
            messages.success(request, 'Artikel wurde erfolgreich erstellt!')
            return redirect('artikel_management', lager_id=lager.id)
    return render(request, 'artikel_create.html', {'form': form, 'lager': lager})


@login_required
def artikel_management(request, lager_id):
    """Übersicht aller Artikel in einem Lager."""
    lager = get_object_or_404(Lager, id=lager_id)
    if request.user not in lager.users.all():
        return redirect('lager_list')
    artikel_list = lager.artikel.all()
    return render(request, 'artikel_management.html', {'lager': lager, 'artikel_list': artikel_list})


# 4. Transaktionen (Ein-/Ausgang)
@login_required
def transaction(request, lager_id):
    """Führt eine Transaktion (Warenein-/ausgang) durch."""
    lager = get_object_or_404(Lager, id=lager_id)
    if request.method == "POST":
        transaction_type = request.POST.get("transaction_type")
        article_id = request.POST.get("article")
        quantity = int(request.POST.get("quantity"))
        article = get_object_or_404(Artikel, id=article_id, lager=lager)

        if transaction_type == "in":
            article.menge += quantity
        elif transaction_type == "out" and article.menge >= quantity:
            article.menge -= quantity
        else:
            messages.error(request, "Nicht genügend Artikel für den Abgang verfügbar!")
            return redirect('transaction', lager_id=lager.id)

        article.save()
        Transaction.objects.create(article=article, lager=lager, type=transaction_type, quantity=quantity)
        messages.success(request, 'Transaktion erfolgreich durchgeführt!')
        return redirect('lager_detail', lager_id=lager.id)
    return render(request, 'transaction.html', {'lager': lager})


# 5. Bewegungsprotokoll
@login_required
def transaction_log(request, lager_id):
    """Zeigt das Bewegungsprotokoll mit Filteroptionen."""
    lager = get_object_or_404(Lager, id=lager_id)
    if request.user not in lager.users.all():
        messages.error(request, "Du hast keinen Zugriff auf dieses Lager.")
        return redirect('lager_list')

    # Filteroptionen
    transaction_type = request.GET.get('type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    transactions = Transaction.objects.filter(lager=lager).order_by('-date')
    if transaction_type in ['in', 'out']:
        transactions = transactions.filter(type=transaction_type)
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    return render(request, 'transaction_log.html', {'lager': lager, 'transactions': transactions})


# 6. CSV-Export für Bewegungsprotokoll und Speicherung
@login_required
def transaction_export_csv(request, lager_id):
    """Exportiert das Bewegungsprotokoll als CSV-Datei und speichert sie im MEDIA-Ordner."""
    lager = get_object_or_404(Lager, id=lager_id)
    if request.user not in lager.users.all():
        messages.error(request, "Du hast keinen Zugriff auf dieses Lager.")
        return redirect('lager_list')

    transactions = Transaction.objects.filter(lager=lager).order_by('-date')

    # Datei speichern im MEDIA-Ordner
    file_path = os.path.join(MEDIA_ROOT, f"transaction_log_{lager.name}.csv")
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Datum', 'Artikel', 'Typ', 'Menge'])
        for transaction in transactions:
            writer.writerow([
                localtime(transaction.date).strftime('%Y-%m-%d %H:%M:%S'),
                transaction.article.name,
                transaction.get_type_display(),
                transaction.quantity
            ])
    
    # Datei zum Download bereitstellen
    with open(file_path, 'rb') as csvfile:
        response = HttpResponse(csvfile.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="transaction_log_{lager.name}.csv"'
        return response
