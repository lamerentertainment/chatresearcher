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

CMD ["sh", "-c", "if [ -f skills/${TENANT}/Praejudizen.csv ]; then PYTHONPATH=. python3 scripts/import_data.py skills/${TENANT}/Praejudizen.csv; fi && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
