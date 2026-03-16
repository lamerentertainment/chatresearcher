FROM python:3.11-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode und Daten kopieren
COPY . .

# Port für Cloud Run (Standard ist 8080)
EXPOSE 8080

# Befehl zum Starten: Daten importieren und dann FastAPI starten
# Cloud Run setzt die PORT Umgebungsvariable automatisch
CMD ["sh", "-c", "python import_data.py Präjudizen.csv && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
