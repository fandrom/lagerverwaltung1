Lagerverwaltung 📦

Die Lagerverwaltung ist ein leistungsstarkes Django-Projekt, das darauf abzielt, die Verwaltung von Lagerbeständen, Artikeln und zugehörigen Prozessen wie Ein- und Auslagerung, Bewegungsprotokollierung und Benutzerberechtigungen zu optimieren. Dieses Projekt wurde entwickelt, um eine benutzerfreundliche, effiziente und moderne Lösung für die Lagerverwaltung bereitzustellen.

🚀 Features

    Lagerverwaltung:

        Erstellen, Bearbeiten und Anzeigen von Lagerdetails.

        Benutzerberechtigungen zu Lagern verwalten (Hinzufügen/Entfernen von Benutzern).

    Artikelverwaltung:

        Hinzufügen, Bearbeiten und Löschen von Artikeln in einem Lager.

        Übersicht über den aktuellen Artikelbestand.

    Transaktionsmanagement:

        Ein- und Auslagerung von Artikeln mit Mengenaktualisierung.

        Bewegungsprotokollierung und Filterung nach Typ und Datum.

        Export des Bewegungsprotokolls als CSV-Datei.

    Benutzerfreundlichkeit:

        Intuitive Benutzeroberfläche basierend auf Bootstrap.

        Scrollbare Tabellen und responsive Elemente.

        Echtzeit-Feedback für Aktionen (z. B. Erfolg-/Fehlermeldungen).

    Adminbereich:

        Zugriff auf den Django-Admin zur erweiterten Verwaltung.


🛠️ Technologien

Dieses Projekt wurde mit folgenden Technologien entwickelt:

    Backend:

        Python 3.10+

        Django 4.x

    Frontend:

        HTML5, CSS3, Bootstrap 5.3

        JavaScript für dynamische Funktionen

    Datenbank:

        SQLite (Standard) oder eine andere kompatible Datenbank (z. B. PostgreSQL)

    Sonstiges:

        Bootstrap Icons

        Google Fonts (Mulish)

📂 Projektstruktur:

lagerverwaltung/
├── DjangoProject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── myapp/
│   ├── templates/
│   │   ├── base.html
│   │   ├── lager_list.html
│   │   ├── artikel_management.html
│   │   └── ...
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── static/
│   ├── styles/
│   │   └── style.css
│   └── ...
└── manage.py


⚙️ Installation und Setup:

Folge den untenstehenden Schritten, um das Projekt lokal auszuführen:

1. Repository klonen:

git clone https://github.com/DEIN-BENUTZERNAME/lagerverwaltung.git
cd lagerverwaltung

2. Virtuelle Umgebung erstellen und aktivieren:

python -m venv venv
source venv/bin/activate  # Für Linux/Mac
venv\Scripts\activate     # Für Windows

3. Abhängigkeiten installieren:		pip install -r requirements.txt

4. Datenbank migrieren:			python manage.py makemigrations
					python manage.py migrate

5. Benutzer erstellen (optional): 	python manage.py createsuperuser

6. Server starten:			python manage.py runserver

7.Zugriff auf die Anwendung unter: 	http://127.0.0.1:8000/


🌟 Nutzung

    Lagerliste anzeigen: Alle verfügbaren Lager durchsuchen.

    Artikel bearbeiten und hinzufügen: Lagerbestände aktuell halten.

    Protokoll exportieren: Bewegungsdaten als CSV herunterladen.

📋 To-Do

Geplante Verbesserungen:

- Unterstützung für Mehrsprachigkeit.

- Erweiterung für Lagerkategorien.

- Verbesserte Berichte mit Diagrammen.

- Lagerverwaltung mit eingebautem KI-engine 
	

🤝 Mitwirkende

fandrom -	https://github.com/fandrom
	
Beiträge sind willkommen! Erstelle einen Pull Request oder eröffne ein Issue.


📜 Lizenz

Dieses Projekt steht unter der MIT-Lizenz. ( siehe Lizenz-Datei)

 
 


