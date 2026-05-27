#!/bin/bash
set -euo pipefail

# === Konfiguration ===
SERVER_IP="${SERVER_IP:-178.105.27.61}"
SERVER_USER="root"
REMOTE_SKILLS_DIR="/root/.hermes/skills"
SERVICE="hermes-gateway"
SKILLS=(krg-wissen textbausteine-erstellen)
LOCAL_SKILLS_DIR="$(cd "$(dirname "$0")" && pwd)/skills"

echo "--- 1. Skills via rsync hochladen ---"
for skill in "${SKILLS[@]}"; do
  src="$LOCAL_SKILLS_DIR/$skill/"
  dst="$SERVER_USER@$SERVER_IP:$REMOTE_SKILLS_DIR/$skill/"
  echo "    → $skill"
  rsync -avz --delete \
    --exclude='.DS_Store' \
    --exclude='__pycache__' \
    --exclude='.venv' \
    "$src" "$dst"
done

echo "--- 2. Hermes-Gateway neu starten ---"
ssh "$SERVER_USER@$SERVER_IP" "systemctl restart $SERVICE"

echo "--- 3. Status prüfen ---"
ssh "$SERVER_USER@$SERVER_IP" "systemctl status $SERVICE --no-pager -l | head -20"

echo "--- 4. Letzte Log-Einträge ---"
ssh "$SERVER_USER@$SERVER_IP" "journalctl -u $SERVICE -n 20 --no-pager"

echo "--- Skills-Upload fertig ---"
