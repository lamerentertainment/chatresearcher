## 0. Automatisiertes Deployment (Empfohlen)

Du kannst das gesamte Deployment (Datenimport + Backend + Frontend) mit einem einzigen Befehl ausführen:

```bash
./deploy.sh
```

Dies führt automatisch `import_data.py` aus und lädt anschließend beide Teile der App hoch.

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

### Umgebungsvariablen & Secrets

Die App benötigt folgende Variablen in Cloud Run (unter **Variablen & Geheimnisse**):

| Variable | Beschreibung | Empfehlung |
| :--- | :--- | :--- |
| `ANTHROPIC_API_KEY` | Dein Anthropic API Key | Als **Secret** einbinden |
| `ADMIN_PASSWORD` | Das Passwort für den Admin-Login | Als **Secret** einbinden |
| `JWT_SECRET` | Ein langer Zufallsstring für Session-Sicherung | Als **Secret** einbinden |
| `ALLOWED_FRAME_ANCESTORS` | `https://luch0.sharepoint.com` | Als **Variable** setzen |
| `SECURE_COOKIES` | `true` (für HTTPS/Produktion) | Als **Variable** setzen |
| `CLOUD_RUN_URL` | Die URL des Cloud Run Dienstes (z.B. `https://chat-researcher-xxx-ew.a.run.app`) | Als **Variable** setzen |
| `CORS_ORIGINS` | Kommagetrennte Firebase-Domains (z.B. `https://gen-lang-client-0915148106.web.app,https://gen-lang-client-0915148106.firebaseapp.com`) | Als **Variable** setzen |

#### Einrichten über das Google Cloud Terminal:

```bash
# 1. Secrets erstellen (falls noch nicht vorhanden)
gcloud secrets create ANTHROPIC_API_KEY --replication-policy="automatic"
gcloud secrets create ADMIN_PASSWORD --replication-policy="automatic"
gcloud secrets create JWT_SECRET --replication-policy="automatic"

# 2. Werte hinzufügen (Warten auf Eingabe)
echo -n "DEIN_KEY" | gcloud secrets versions add ANTHROPIC_API_KEY --data-file=-
echo -n "DEIN_PASSWORT" | gcloud secrets versions add ADMIN_PASSWORD --data-file=-
echo -n "MEIN_GEHEIMER_STRING" | gcloud secrets versions add JWT_SECRET --data-file=-

# 3. Cloud Run Dienst aktualisieren, um Secrets zu nutzen
gcloud run services update chat-researcher \
  --set-secrets="ANTHROPIC_API_KEY=ANTHROPIC_API_KEY:latest,ADMIN_PASSWORD=ADMIN_PASSWORD:latest,JWT_SECRET=JWT_SECRET:latest" \
  --set-env-vars="SECURE_COOKIES=true,ALLOWED_FRAME_ANCESTORS=https://luch0.sharepoint.com,CLOUD_RUN_URL=$(gcloud run services describe chat-researcher --region europe-west3 --format 'value(status.url)'),CORS_ORIGINS=https://gen-lang-client-0915148106.web.app,https://gen-lang-client-0915148106.firebaseapp.com" \
  --region europe-west3
```

#### Einrichten über die Google Cloud Console:

1.  Gehe zu **Security > Secret Manager**.
2.  Erstelle die Secrets `ANTHROPIC_API_KEY`, `ADMIN_PASSWORD` und `JWT_SECRET` und füge deine Werte als Versionen hinzu.
3.  Gehe zu deinem **Cloud Run Service > EDIT & DEPLOY NEW REVISION**.
4.  Unter **Variables & Secrets** > Tab **Secrets**:
    - Klicke auf "Add Secret Reference".
    - Wähle das Secret aus (z.B. `ADMIN_PASSWORD`).
    - Wähle "Reference as environment variable".
    - Gib den Namen der Umgebungsvariable ein (muss exakt `ADMIN_PASSWORD` sein).
5.  Unter Tab **Variables**:
    - Füge `SECURE_COOKIES` mit dem Wert `true` hinzu.
    - Füge `ALLOWED_FRAME_ANCESTORS` mit deiner SharePoint URL hinzu.
6.  Klicke auf **Deploy**.

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
