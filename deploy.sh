#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- 1. Importiere Präjudizen ---"
python import_data.py Präjudizen.csv

echo "--- 2. Backend Deployment (Cloud Run) ---"
gcloud run deploy chat-researcher \
    --source . \
    --region europe-west3 \
    --allow-unauthenticated

echo "--- 3. Frontend Deployment (Firebase Hosting) ---"
firebase deploy --only hosting

echo "--- Deployment erfolgreich abgeschlossen ---"
