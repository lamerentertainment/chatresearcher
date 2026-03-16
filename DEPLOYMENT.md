# Deployment Guide: Chat Researcher (Cloud Run + Firebase)

Diese Anleitung erklärt Schritt für Schritt, wie du die Anwendung auf Google Cloud Run und Firebase Hosting veröffentlichst.

## 1. Voraussetzungen

*   **Google Cloud SDK (gcloud CLI)**: [Installationsanleitung](https://cloud.google.com/sdk/docs/install)
*   **Firebase CLI**: `npm install -g firebase-tools`
*   **Docker**: Muss auf deinem Rechner laufen, um das Container-Image zu bauen.
*   **Projekt-ID**: Deine ID ist `gen-lang-client-0915148106`.

## 2. Vorbereitung (Einmalig)

Logge dich in die CLIs ein:
```bash
gcloud auth login
firebase login
```

Setze dein Standardprojekt für `gcloud`:
```bash
gcloud config set project gen-lang-client-0915148106
```

## 3. Backend Deployment (Cloud Run)

Da dein Backend in Python geschrieben ist, wird es als Container auf Cloud Run gehostet.

Führe diesen Befehl im Hauptverzeichnis aus:
```bash
gcloud run deploy chat-researcher \
    --source . \
    --region europe-west3 \
    --allow-unauthenticated
```

### Wichtig: Umgebungsvariablen setzen
Die `.env` Datei wird aus Sicherheitsgründen **nicht** hochgeladen. Du musst die Variablen direkt in Cloud Run hinterlegen:

1.  Öffne die [Cloud Run Konsole](https://console.cloud.google.com/run).
2.  Wähle `chat-researcher` aus.
3.  Klicke auf **"Neue Revision bearbeiten"**.
4.  Füge unter **"Variablen & Geheimnisse"** mindestens folgende hinzu:
    *   `ANTHROPIC_API_KEY`: Dein API Schlüssel von Anthropic.
    *   `JWT_SECRET`: Ein langer, zufälliger String für die Session-Sicherheit.
    *   `ALLOWED_FRAME_ANCESTORS`: Deine SharePoint URL (z.B. `https://tenant.sharepoint.com`).

## 4. Frontend Deployment (Firebase Hosting)

Firebase Hosting dient als "Eingangstor" und leitet Anfragen an das Backend weiter.

Führe diesen Befehl aus:
```bash
firebase deploy --only hosting
```

## 5. SharePoint Integration (Iframe)

Damit die Seite in SharePoint angezeigt werden kann:

1.  **HTTPS**: Die App muss über HTTPS laufen (wird von Firebase/Cloud Run automatisch bereitgestellt).
2.  **HTML-Feldsicherheit**: In den SharePoint Website-Einstellungen muss die Domain `gen-lang-client-0915148106.web.app` als vertrauenswürdig für Iframes hinzugefügt werden.
3.  **Middleware**: Die App setzt bereits den `frame-ancestors` Header (siehe `app/main.py`), sofern du `ALLOWED_FRAME_ANCESTORS` in den Cloud-Variablen gesetzt hast.

## 6. Besonderheiten (SQLite)

Da Cloud Run "stateless" ist:
*   Die **Präjudizen** werden bei jedem Start automatisch aus der `Präjudizen.csv` in SQLite importiert.
*   **Benutzer-Accounts** gehen verloren, wenn die App neu startet (da die `users.db` gelöscht wird). Für eine dauerhafte Speicherung müsste später eine externe Datenbank wie *Google Cloud SQL* angebunden werden.
