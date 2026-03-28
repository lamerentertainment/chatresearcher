#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

SERVICE="chat-researcher"
REGION="europe-west3"
PROJECT_ID="gen-lang-client-0915148106"
FIREBASE_DOMAINS="https://${PROJECT_ID}.web.app,https://${PROJECT_ID}.firebaseapp.com"

# ANTHROPIC_API_KEY aus .env laden falls nicht bereits gesetzt
if [ -z "$ANTHROPIC_API_KEY" ] && [ -f .env ]; then
  export ANTHROPIC_API_KEY=$(grep '^ANTHROPIC_API_KEY=' .env | cut -d '=' -f2-)
fi

echo "--- 1. Importiere Präjudizen ---"
python import_data.py Präjudizen.csv

echo "--- 1b. Skills zur Anthropic API hochladen ---"
python deploy_skills.py

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

# ^|^ als Trennzeichen, damit das Komma in CORS_ORIGINS nicht als Env-Var-Separator gilt
gcloud run services update $SERVICE \
    --region $REGION \
    --update-env-vars "^|^CLOUD_RUN_URL=${CLOUD_RUN_URL}|CORS_ORIGINS=${FIREBASE_DOMAINS}"

echo "--- 4. Frontend Deployment (Firebase Hosting) ---"
firebase deploy --only hosting

echo "--- Deployment erfolgreich abgeschlossen ---"
