# Multi-Tenant-Architektur & Benutzerdefinierte Skills / Prompts

Dieses Dokument beschreibt die Konzepte und Implementierungsschritte, um die Chat-Researcher-Anwendung für mehrere Gerichte (Multi-Tenancy) anzupassen und Benutzern/Administratoren zu ermöglichen, System-Prompts, Welcome-Messages sowie Skills direkt über die Benutzeroberfläche zu steuern.

---

## Konzept 1: Konfigurationsgesteuerte Multi-Tenancy (Code-Sharing)

Um denselben Code für verschiedene Gerichtsinstanzen zu nutzen und Updates zentral einzupflegen, werden gerichtsbezogene Details aus dem Code in Umgebungsvariablen (`.env`) und externe Konfigurationsdateien ausgelagert.

### 1. System-Prompt auslagern
Der System-Prompt wird nicht mehr hartcodiert in [chat.py](file:///Users/jonasachermann/repos/chatresearcher/app/chat.py) hinterlegt, sondern aus einer Datei geladen, deren Pfad in der `.env` definiert ist:
* **Umgebungsvariable**: `SYSTEM_PROMPT_PATH=prompts/luzern_kriminalgericht.txt`
* **Implementierung**:
  ```python
  from pathlib import Path
  import os

  SYSTEM_PROMPT_PATH = os.getenv("SYSTEM_PROMPT_PATH", "prompts/default_prompt.txt")

  def load_system_prompt() -> str:
      return Path(SYSTEM_PROMPT_PATH).read_text(encoding="utf-8")
  ```

### 2. Dynamische Skills und IDs
Verzeichnisse und Skill-ID-Konfigurationen werden ebenfalls flexibel gehalten:
* **Umgebungsvariable**: `SKILLS_DIR=skills/luzern` und `SKILL_IDS_FILE=skill_ids_luzern.json`
* **Implementierung in [skills_config.py](file:///Users/jonasachermann/repos/chatresearcher/app/skills_config.py)**:
  ```python
  SKILL_IDS_FILE = os.getenv("SKILL_IDS_FILE", "skill_ids.json")
  _SKILL_IDS_PATH = Path(__file__).parent.parent / SKILL_IDS_FILE
  ```

### 3. Datenbank-Trennung
Die SQLite-Datenbank bzw. kantonale Präjudizen können für jede Instanz separat angegeben werden:
* **Umgebungsvariable**: `DB_PATH=data/luzern_praejudizen.db`

---

## Konzept 2: Dynamische Anpassung per Datenbank & Frontend (Live-Edit)

Sollen Administratoren oder Benutzer System-Prompts, Begrüssungstexte und Skills direkt im Browser ändern können, wird die Konfiguration in **Google Cloud Firestore** verwaltet.

### 1. Datenmodell (Firestore)

* **Collection `settings` (Dokument `general`):**
  ```json
  {
    "system_prompt": "Du bist ein juristischer Rechercheassistent...",
    "welcome_message": "Guten Tag! Ich bin..."
  }
  ```
* **Collection `skills` (Ein Dokument pro Skill):**
  ```json
  {
    "id": "krg-wissen",
    "name": "KRG Wissensmanagement",
    "content": "# SKILL.md Inhalt...\n- Anleitung...",
    "claude_skill_id": "sk_12345",
    "is_active": true
  }
  ```

### 2. API-Endpoints ([main.py](file:///Users/jonasachermann/repos/chatresearcher/app/main.py))

Wir definieren API-Routen, um diese Daten abzufragen und zu aktualisieren:

* **Öffentlich (für das Chat-Frontend):**
  - `GET /api/config`: Liefert die aktuelle `welcome_message` für den Startbildschirm.
* **Admin-geschützt (nur für Superuser):**
  - `GET /api/admin/config`: Gibt den editierbaren System-Prompt und die Welcome-Message zurück.
  - `POST /api/admin/config`: Aktualisiert die Einstellungen.
  - `GET /api/admin/skills`: Listet alle vorhandenen Skills auf.
  - `POST /api/admin/skills`: Legt neue Skills an oder aktualisiert bestehende.
  - `DELETE /api/admin/skills/{id}`: Löscht einen Skill.

### 3. Anpassungen in [chat.py](file:///Users/jonasachermann/repos/chatresearcher/app/chat.py)

Der Prompt und die Skills werden vor dem Start eines Chats direkt aus Firestore abgefragt statt aus dem lokalen Dateisystem geladen zu werden:

```python
async def get_active_config_from_db():
    # 1. System Prompt aus Firestore laden
    prompt_doc = await firestore_db.collection("settings").document("general").get()
    system_prompt = prompt_doc.to_dict().get("system_prompt") if prompt_doc.exists else DEFAULT_SYSTEM_PROMPT
    
    # 2. Aktive Skills aus Firestore laden
    skills_docs = await firestore_db.collection("skills").where("is_active", "==", True).get()
    
    skill_ids = []
    skill_names = []
    local_skills_list = []
    
    for doc in skills_docs:
        data = doc.to_dict()
        skill_names.append(data["name"])
        if data.get("claude_skill_id"):
            skill_ids.append(data["claude_skill_id"])
        local_skills_list.append(f"### Skill: {data['name']}\n{data['content']}")
        
    local_skills_prompt = ""
    if local_skills_list:
        local_skills_prompt = "\n\n--- LOCAL SKILLS ---\n\n" + "\n\n".join(local_skills_list)
        
    return system_prompt, skill_ids, skill_names, local_skills_prompt
```

### 4. Admin-Einstellungen im Frontend

1. **Begrüssungsnachricht dynamisieren ([chat.html](file:///Users/jonasachermann/repos/chatresearcher/static/chat.html))**:
   Beim Laden der Seite ruft das JS `fetch('/api/config')` auf, rendert den zurückgegebenen Markdown-Willkommenstext und befüllt den Begrüssungs-Chat-Bubble.
2. **Admin-Einstellungsseite erstellen (`static/admin_settings.html`)**:
   * **System-Prompt-Editor**: `<textarea>` für den System-Prompt.
   * **Willkommensnachricht-Editor**: `<textarea>` für den Begrüssungstext.
   * **Skill-Manager**: Liste/Tabelle aller Skills mit Möglichkeit zur Bearbeitung (Markdown-Inhalt, Name, `is_active`-Schalter) und Löschung.

---

## Optionale Erweiterung: Personalisierte Workspaces pro Benutzer
Wenn jeder einzelne User seine eigenen Prompts/Skills konfigurieren darf (statt einer gerichtsweiten Einstellung):
1. Verknüpfen Sie die Firestore-Dokumente mit der jeweiligen `user_id`:
   - `users/{user_id}/settings/general`
   - `users/{user_id}/skills/{skill_id}`
2. Ermitteln Sie die `user_id` über die FastAPI-Benutzerverwaltung (`current_active_user_simplified`) bei jedem Aufruf von `/chat` und laden Sie ausschliesslich die benutzerdefinierten Daten dieser ID.
