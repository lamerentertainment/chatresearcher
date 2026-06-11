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

## 4. Verbindung zu Firestore wählen

Du kannst den lokalen Server entweder mit der **aktiven (live) Cloud-Datenbank** verbinden oder den **lokalen Emulator** nutzen.

### Option A: Mit der aktiven Firestore-Instanz (GCP Cloud) verbinden [Empfohlen]
Der Server kontaktiert direkt die echte Cloud-Datenbank.
1. Stelle sicher, dass die Umgebungsvariable `FIRESTORE_EMULATOR_HOST` **nicht** gesetzt ist. Falls sie in deinem Terminal aktiv ist, entferne sie mit:
   ```bash
   unset FIRESTORE_EMULATOR_HOST
   ```
2. Falls du noch nicht autorisiert bist, melde dich bei Google Cloud an, damit die Anwendung deine Standard-GCP-Zugangsdaten (Application Default Credentials) nutzen kann:
   ```bash
   gcloud auth application-default login
   ```
3. Starte den Server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Option B: Lokalen Firestore Emulator nutzen
Falls du Änderungen isoliert testen möchtest:
1. Firestore Emulator starten:
   ```bash
   firebase emulators:start
   ```
2. Setze die Emulator-Variable im Server-Terminal und starte den Server:
   ```bash
   export FIRESTORE_EMULATOR_HOST="localhost:8080"
   uvicorn app.main:app --reload
   ```
   Das Emulator-UI ist anschliessend unter [http://localhost:4000](http://localhost:4000) erreichbar.
