from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URLs der Django-Anwendung
urlpatterns = [
    # Authentifizierung
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        next_page='lager_list'  # Nach Login zur Lagerliste weiterleiten
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Nach Logout zur Login-Seite

    # Registrierung
    path('register/', views.register, name='register'),

    # Lagerverwaltung
    path('lager/', views.lager_list, name='lager_list'),  # Liste aller Läger anzeigen
    path('lager/create/', views.lager_create, name='lager_create'),  # Neues Lager erstellen
    path('lager/<int:lager_id>/', views.lager_detail, name='lager_detail'),  # Details eines spezifischen Lagers
    path('lager/<int:lager_id>/grant_access/', views.grant_access, name='grant_access'),  # Benutzerberechtigungen zuweisen
    path('lager/<int:lager_id>/remove_user/<int:user_id>/', views.remove_user_from_lager, name='remove_user_from_lager'),  # Benutzer entfernen

    # Artikelverwaltung
    path('lager/<int:lager_id>/artikel_management/', views.artikel_management, name='artikel_management'),  # Artikelübersicht anzeigen
    path('lager/<int:lager_id>/artikel_management/artikel_create/', views.artikel_create, name='artikel_create'),  # Artikel hinzufügen
    path('lager/<int:lager_id>/artikel_management/<int:id>/edit/', views.artikel_edit, name='artikel_edit'),  # Artikel bearbeiten

    # Lagerbestand
    path('lager/<int:lager_id>/current_status/', views.current_status, name='current_status'),  # Artikelbestand anzeigen

    # Transaktionen
    path('lager/<int:lager_id>/transaction/', views.transaction, name='transaction'),  # Artikel ein- oder auslagern
    path('lager/<int:lager_id>/transaction-log/', views.transaction_log, name='transaction_log'),  # Bewegungsprotokoll anzeigen
    path('lager/<int:lager_id>/transaction-export/', views.transaction_export_csv, name='transaction_export_csv'),  # Bewegungsprotokoll als CSV exportieren
]

# Medien-Dateien in der Entwicklungsumgebung verfügbar machen
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
