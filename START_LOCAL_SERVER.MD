# Lokal Server Starten

Um den Chat-Researcher lokal auszuführen, folge diesen Schritten:

## 1. Virtuelle Umgebung aktivieren
Stelle sicher, dass du dich im Hauptverzeichnis des Projekts befindest.
```bash
source .venv/bin/activate
```

## 2. (Optional) Daten importieren
Falls die SQLite-Datenbank noch nicht existiert oder du die Daten neu einlesen möchtest:
```bash
PYTHONPATH=. python3 scripts/import_data.py Präjudizen.csv
```

## 3. Server starten
Starte den FastAPI-Server mit uvicorn. Der Parameter `--reload` sorgt dafür, dass der Server bei Codeänderungen automatisch neu startet.
```bash
uvicorn app.main:app --reload
```

Der Server ist anschließend unter [http://127.0.0.1:8000](http://127.0.0.1:8000) erreichbar.
