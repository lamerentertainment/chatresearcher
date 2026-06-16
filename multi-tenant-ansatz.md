# Multi-Tenant-Architektur & Skill-Verwaltung (Ansatz A: Datei- & Git-basiert)

Dieses Dokument beschreibt die implementierte mandantenfähige Architektur (Multi-Tenancy) für die Chatbot-Instanzen sowie die Vorgehensweise zur Konfiguration, lokalen Ausführung und Bereitstellung neuer Gerichtsinstanzen.

---

## Architektur-Übersicht

Um maximale Stabilität zu gewährleisten, von gemeinsamen Core-Code-Updates zu profitieren und Merge-Konflikte zu vermeiden, teilen sich alle Instanzen dieselbe Codebase. Die Steuerung der jeweiligen Instanz erfolgt über die Umgebungsvariable `TENANT` und die entsprechende Unterordner-Struktur im [skills/](file:///Users/jonasachermann/repos/chatresearcher/skills)-Verzeichnis.

### 1. Verzeichnisstruktur
Die Skills (Anleitungen, Indizes, Textbausteine) und die Anthropic-Skill-IDs sind nach Mandanten (Tenants) getrennt abgelegt:

```text
skills/
├── krg/                          # Haupt-Tenant (Kriminalgericht Luzern)
│   ├── skill_ids.json            # Deployed Skill-IDs für Anthropic
│   ├── krg-wissen/
│   │   ├── SKILL.md
│   │   └── resources/
│   └── textbausteine-erstellen/
│       ├── SKILL.md
│       └── resources/
└── dummy/                        # Beispiel/Test-Tenant
    ├── skill_ids.json            # Deployed Skill-IDs (z. B. leeres {} vor Erstdeploy)
    └── dummy-wissen/
        ├── SKILL.md
        └── resources/
            └── dummy_doc.md
```

### 2. Implementierte Code-Anpassungen
*   **[skills_config.py](file:///Users/jonasachermann/repos/chatresearcher/app/skills_config.py)**: Lädt die `skill_ids.json` dynamisch aus dem Pfad `skills/<TENANT>/skill_ids.json`.
*   **[chat.py](file:///Users/jonasachermann/repos/chatresearcher/app/chat.py)**: Aggregiert lokale Skills über `_load_local_skills()` dynamisch aus dem Pfad `skills/<TENANT>/`.
*   **[tools.py](file:///Users/jonasachermann/repos/chatresearcher/app/tools.py)**: Stellt die dem Modell angebotenen Tools mandantenspezifisch zusammen (`get_tool_definitions(tenant)`). Die lokalen SQLite-Präjudizen-Tools (`list_regesten`, `get_praejudiz`, `search_local_cases`) werden nur für Mandanten in `LOCAL_DB_TENANTS` angeboten; alle Mandanten erhalten die OpenCaseLaw-MCP-Tools. Siehe [Tenant-spezifische Tools](#tenant-spezifische-tools-und-skills) unten.
*   **[deploy_skills.py](file:///Users/jonasachermann/repos/chatresearcher/scripts/deploy_skills.py)**: Liest und aktualisiert die Skills für den übergebenen Mandanten in `skills/<TENANT>/`.
*   **[main.py](file:///Users/jonasachermann/repos/chatresearcher/app/main.py)**: Loggt Anfragen unter Angabe des aktuellen `tenant` in Firestore und filtert die Admin-Anfragen-Historie entsprechend, um Datenvermischung zu vermeiden.
*   **[deploy.sh](file:///Users/jonasachermann/repos/chatresearcher/deploy.sh)**: Automatisiert das Aufteilen der Dokumentenvorlagen für den aktiven Mandanten und benennt den Google Cloud Run Service dynamisch in `chat-researcher-<tenant>` um.
*   **[upload-skills-to-hermes.sh](file:///Users/jonasachermann/repos/chatresearcher/upload-skills-to-hermes.sh)**: Erkennt die Skill-Unterordner unter `skills/<TENANT>/` automatisch und synchronisiert diese auf den Hermes-Gateway-Server.

---

## Tenant-spezifische Tools und Skills

Neben den datei-/Git-basierten Skills (oben) gibt es zwei weitere mandantenabhängige Mechanismen, die leicht zu Datenvermischung zwischen Mandanten führen können, wenn sie global statt pro Tenant behandelt werden. Beide wurden anhand des `kg3abt`-Mandanten korrigiert.

### Tools (lokale DB vs. OpenCaseLaw)
Die dem Modell angebotenen Tool-Definitionen in [tools.py](file:///Users/jonasachermann/repos/chatresearcher/app/tools.py) sind **nicht** für alle Mandanten identisch:

*   **OpenCaseLaw-MCP-Tools** (`search_decisions`, `find_leading_cases`, `get_law`, `get_commentary`, …): für **alle** Mandanten verfügbar.
*   **Lokale SQLite-Präjudizen-Tools** (`list_regesten`, `get_praejudiz`, `search_local_cases`): greifen auf die KRG-spezifische DB `data/praejudizen.db` zu und werden **nur** für Mandanten in `LOCAL_DB_TENANTS` (aktuell `{"krg"}`) angeboten.

Begründung: Mandanten ohne eigene Präjudizen-DB (z. B. `kg3abt`) führen ihre internen Wissensdokumente ausschliesslich im Skill-Wiki. Würden ihnen die DB-Tools trotzdem angeboten, ruft das Modell z. B. `list_regesten` auf und meldet fälschlich „keine internen Wissensdokumente vorhanden", weil die (fremde, leere) KRG-DB abgefragt wird.

`execute_tool()` enthält zusätzlich eine Schutzschicht: ein DB-Tool-Aufruf durch einen Nicht-`LOCAL_DB_TENANTS`-Mandanten (z. B. aus altem Chat-Verlauf) wird abgefangen und verweist auf den Wissens-Skill.

> **Neuen Mandanten mit eigener Präjudizen-DB anlegen:** Tenant zu `LOCAL_DB_TENANTS` in `tools.py` hinzufügen **und** eine `skills/<TENANT>/Praejudizen.csv` bereitstellen (wird von `deploy.sh` automatisch in die DB importiert).

### Skill-Quellen: Datei (`skill_ids.json`) **und** Firestore
`load_tenant_skills()` in [chat.py](file:///Users/jonasachermann/repos/chatresearcher/app/chat.py) führt **zwei** Skill-Quellen zusammen:

1.  **Datei-basierte Skills** (`skills/<TENANT>/skill_ids.json`, befüllt durch `deploy_skills.py`): Dies sind die tatsächlichen Anthropic-**Container-Skills**, die der Claude-Pfad anhängt. Sie werden **immer** geladen.
2.  **Firestore-Admin-Skills** (`settings`/`skills`-Collection, über die Admin-Oberfläche gepflegt): liefern Skill-**Inhalt** (genutzt vom Hermes-Pfad als `--- LOCAL SKILLS ---`-Prompt) sowie optional eine `claude_skill_id` für zusätzliche Container-Skills.

> **Wichtig (behobener Fehler):** Früher ersetzten Firestore-Skills die datei-basierten Skills vollständig, sobald *irgendein* Firestore-Skill existierte. Da über die Admin-UI angelegte Skills **keine** `claude_skill_id` tragen (`save_admin_skill` speichert dieses Feld nicht), wurde dadurch der deployte Container-Skill (z. B. `kg3abt-wissen`) still abgehängt → das Modell meldete, der Skill stehe „nicht als Werkzeug zur Verfügung". Heute werden beide Quellen **gemerged**.

> **Offene Lücke:** Über die Admin-UI erstellte Skills wirken derzeit nur auf dem Hermes-Pfad (Content im Systemprompt), nicht als Claude-Container-Skill — dafür müsste `save_admin_skill` den Skill zur Anthropic Skills API hochladen und die resultierende `claude_skill_id` mitspeichern.

---

## Admin-Leitfaden: Verwaltung von Instanzen

### 1. Einen neuen Mandanten (Tenant) hinzufügen
Um ein neues Gericht anzulegen:
1.  Erstelle unter `skills/` einen neuen Unterordner, z. B. `skills/zuerich/`.
2.  Erstelle darin eine leere `skill_ids.json` mit folgendem Inhalt:
    ```json
    {}
    ```
3.  Lege die gewünschten Skill-Unterordner an (z. B. `zvr-wissen/`), jeder mit einer `SKILL.md` als Einstiegspunkt.
4.  *(Optional)* Hinterlege Dokumentenvorlagen für die automatische Generierung (z. B. Anpassungen in `deploy.sh` für Docx-Dateien des neuen Mandanten).

### 2. Lokale Entwicklung & Testen
Du kannst verschiedene Instanzen parallel auf unterschiedlichen Ports lokal ausführen, indem du die `TENANT`-Variable beim Starten übergibst:

*   **Instanz KRG starten (Port 8000):**
    ```bash
    # Nutzt standardmässig TENANT=krg aus der .env
    uvicorn app.main:app --reload
    ```
*   **Instanz Dummy-Gericht starten (Port 8001):**
    ```bash
    TENANT=dummy uvicorn app.main:app --reload --port 8001
    ```

### 3. Skills deployen (Anthropic API)
Um die lokalen Verzeichnisse eines Mandanten zur Anthropic API hochzuladen und die `skill_ids.json` des Mandanten zu befüllen:

```bash
# Für KRG
TENANT=krg python3 scripts/deploy_skills.py

# Für Dummy
TENANT=dummy python3 scripts/deploy_skills.py
```

### 4. Cloud Deployment (Google Cloud Run)
Um einen isolierten Dienst für einen Mandanten zu deployen:

```bash
# Bereitstellen für KRG (erstellt Service: chat-researcher-krg)
TENANT=krg ./deploy.sh

# Bereitstellen für Dummy (erstellt Service: chat-researcher-dummy)
TENANT=dummy ./deploy.sh
```

Dadurch erhält jeder Mandant eine eigene, sichere URL in der Google Cloud, während der Quellcode in einem einzigen Repository gepflegt wird.
