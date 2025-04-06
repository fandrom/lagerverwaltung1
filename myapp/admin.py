from django.contrib import admin
from .models import Lager, Artikel, Transaction, LagerAccess

@admin.register(Lager)
class LagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')  # Zeigt Name des Lagers und Besitzer im Admin
    search_fields = ('name', 'owner__username')  # Ermöglicht Suche nach Lagername oder Besitzer
    filter_horizontal = ('users',)  # Ermöglicht einfache Benutzerverwaltung bei Many-to-Many

@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('name', 'menge', 'lager')  # Zeigt Artikelname, Menge und zugehöriges Lager
    list_filter = ('lager',)  # Filteroption nach Lager
    search_fields = ('name', 'lager__name')  # Suche nach Artikelname und Lagername

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'article', 'type', 'quantity', 'lager')  # Zeigt wichtige Details der Transaktion
    list_filter = ('type', 'lager', 'date')  # Ermöglicht Filterung nach Typ, Lager und Datum
    search_fields = ('article__name', 'lager__name')  # Suche nach Artikelname oder Lagername

@admin.register(LagerAccess)
class LagerAccessAdmin(admin.ModelAdmin):
    list_display = ('lager', 'user')  # Zeigt Lager und Benutzer
    search_fields = ('lager__name', 'user__username')  # Ermöglicht Suche nach Lager oder Benutzername
