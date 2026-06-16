#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Wenn TENANT nicht in der Umgebung gesetzt ist, versuchen wir es aus .env zu lesen
if [ -z "$TENANT" ] && [ -f .env ]; then
  TENANT=$(grep '^TENANT=' .env | cut -d '=' -f2-)
fi
TENANT="${TENANT:-krg}"
SERVICE="${SERVICE:-chat-researcher-$TENANT}"
REGION="europe-west3"
PROJECT_ID="gen-lang-client-0915148106"
FIREBASE_DOMAINS="https://${PROJECT_ID}.web.app,https://${PROJECT_ID}.firebaseapp.com"

# Umgebungsvariablen aus .env.<tenant> oder .env laden falls nicht bereits gesetzt
ENV_FILE=".env"
if [ -f ".env.$TENANT" ]; then
  ENV_FILE=".env.$TENANT"
fi

if [ -f "$ENV_FILE" ]; then
  [ -z "$ANTHROPIC_API_KEY" ] && export ANTHROPIC_API_KEY=$(grep '^ANTHROPIC_API_KEY=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$ADMIN_PASSWORD" ] && export ADMIN_PASSWORD=$(grep '^ADMIN_PASSWORD=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$JWT_SECRET" ] && export JWT_SECRET=$(grep '^JWT_SECRET=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$ALLOWED_FRAME_ANCESTORS" ] && export ALLOWED_FRAME_ANCESTORS=$(grep '^ALLOWED_FRAME_ANCESTORS=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$SECURE_COOKIES" ] && export SECURE_COOKIES=$(grep '^SECURE_COOKIES=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$HERMES_API_KEY" ] && export HERMES_API_KEY=$(grep '^HERMES_API_KEY=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$HERMES_URL" ] && export HERMES_URL=$(grep '^HERMES_URL=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$HERMES_REMOTE_API_KEY" ] && export HERMES_REMOTE_API_KEY=$(grep '^HERMES_REMOTE_API_KEY=' "$ENV_FILE" | cut -d '=' -f2-)
  [ -z "$HERMES_REMOTE_URL" ] && export HERMES_REMOTE_URL=$(grep '^HERMES_REMOTE_URL=' "$ENV_FILE" | cut -d '=' -f2-)
fi

echo "--- 1. Importiere Präjudizen ---"
rm -f data/praejudizen.db
if [ -f "skills/$TENANT/Praejudizen.csv" ]; then
  PYTHONPATH=. python3 scripts/import_data.py "skills/$TENANT/Praejudizen.csv"
else
  echo "    → Keine Präjudizen-CSV für Tenant $TENANT gefunden. Überspringe Import."
fi

echo "--- 1b. Rechtliche Textbausteine aktualisieren ---"
if [ -f "skills/$TENANT/TB-Strafrecht.docx" ]; then
  python3 scripts/split_docx_to_md.py "skills/$TENANT/TB-Strafrecht.docx" "./skills/$TENANT/textbausteine-erstellen/resources/"
else
  echo "    → Keine Textbausteine-Docx für Tenant $TENANT gefunden. Überspringe Aktualisierung."
fi


echo "--- 1c. Skills zur Anthropic API hochladen ---"
python3 scripts/deploy_skills.py


echo "--- 2. Backend Deployment (Cloud Run) ---"
gcloud run deploy $SERVICE \
    --source . \
    --region $REGION \
    --allow-unauthenticated

echo "--- 3. CLOUD_RUN_URL und CORS_ORIGINS setzen ---"
CLOUD_RUN_URL=$(gcloud run services describe $SERVICE \
    --region $REGION \
    --format 'value(status.url)')
echo "    → $CLOUD_RUN_URL"

# Dynamisch die Umgebungsvariablen für gcloud zusammenbauen (verhindert das Überschreiben mit leeren Werten)
ENV_VARS="CLOUD_RUN_URL=${CLOUD_RUN_URL}|CORS_ORIGINS=${FIREBASE_DOMAINS}|TENANT=${TENANT}|GOOGLE_CLOUD_PROJECT=${PROJECT_ID}"

[ -n "$ANTHROPIC_API_KEY" ] && ENV_VARS="${ENV_VARS}|ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}"
[ -n "$ADMIN_PASSWORD" ] && ENV_VARS="${ENV_VARS}|ADMIN_PASSWORD=${ADMIN_PASSWORD}"
[ -n "$JWT_SECRET" ] && ENV_VARS="${ENV_VARS}|JWT_SECRET=${JWT_SECRET}"
[ -n "$ALLOWED_FRAME_ANCESTORS" ] && ENV_VARS="${ENV_VARS}|ALLOWED_FRAME_ANCESTORS=${ALLOWED_FRAME_ANCESTORS}"
[ -n "$SECURE_COOKIES" ] && ENV_VARS="${ENV_VARS}|SECURE_COOKIES=${SECURE_COOKIES}"

[ -n "$HERMES_API_KEY" ] && ENV_VARS="${ENV_VARS}|HERMES_API_KEY=${HERMES_API_KEY}"
[ -n "$HERMES_URL" ] && ENV_VARS="${ENV_VARS}|HERMES_URL=${HERMES_URL}"
[ -n "$HERMES_REMOTE_API_KEY" ] && ENV_VARS="${ENV_VARS}|HERMES_REMOTE_API_KEY=${HERMES_REMOTE_API_KEY}"
[ -n "$HERMES_REMOTE_URL" ] && ENV_VARS="${ENV_VARS}|HERMES_REMOTE_URL=${HERMES_REMOTE_URL}"

# ^|^ als Trennzeichen, damit das Komma in CORS_ORIGINS nicht als Env-Var-Separator gilt
gcloud run services update $SERVICE \
    --region $REGION \
    --update-env-vars "^|^${ENV_VARS}"

echo "--- 4. Frontend Deployment (Firebase Hosting) ---"
firebase deploy --only hosting

echo "--- Deployment erfolgreich abgeschlossen ---"
