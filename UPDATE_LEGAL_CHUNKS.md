# Update der rechtlichen Textbausteine

Um die Textbausteine aus der Word-Datei (`./TB-Strafrecht.docx`) zu extrahieren und im Skill `textbausteine-erstellen` zu aktualisieren, führen Sie folgenden Befehl im Hauptverzeichnis aus:

```bash
python3 scripts/split_docx_to_md.py ./TB-Strafrecht.docx ./skills/textbausteine-erstellen/resources/
```

## Was das Skript macht:
1.  **Extraktion**: Liest den Text aus der `.docx`-Datei aus.
2.  **Modularisierung**: Zerlegt den Text anhand der `#Beginn`- und `#Ende`-Markierungen in einzelne `.md`-Dateien.
3.  **Organisation**: Speichert die Dateien im Unterordner `resources/tb/` ab.
4.  **Normalisierung**: Stellt sicher, dass das End-Tag (`#Ende [ID]#`) immer exakt zum ID-Tag im Header passt.
5.  **Index**: Erstellt eine `index.md` im Ordner `resources/tb/` mit einer Übersicht aller Bausteine.

## Voraussetzungen
Das Skript benötigt eine Standard-Python-Installation (Python 3.x). Es werden keine externen Bibliotheken benötigt, da `zipfile` und `xml.etree.ElementTree` verwendet werden.
