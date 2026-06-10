#!/bin/bash
set -euo pipefail

# === Konfiguration ===
SERVER_IP="${SERVER_IP:-178.105.27.61}"
SERVER_USER="root"
REMOTE_SKILLS_DIR="/root/.hermes/skills"
SERVICE="hermes-gateway"
TENANT="${TENANT:-krg}"
LOCAL_SKILLS_DIR="$(cd "$(dirname "$0")" && pwd)/skills/$TENANT"

# Dynamically detect skill subfolders
SKILLS=()
if [ -d "$LOCAL_SKILLS_DIR" ]; then
  for d in "$LOCAL_SKILLS_DIR"/*/; do
    if [ -d "$d" ]; then
      SKILLS+=("$(basename "$d")")
    fi
  done
fi

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
