---
title: Dateistruktur der Wissensdatenbank (raw/)
created: 2026-06-12
last_updated: 2026-06-12
source_count: 0
status: reviewed
location: raw/
---

Diese Seite dokumentiert, wo die Quelldokumente im Verzeichnis `raw/` abgelegt sind. `raw/` spiegelt die Ablage auf der Wissensdatenbank der 3. Abteilung des Kantonsgerichts Luzern (KG3ABT) und wird nie verändert. Schwerpunkt des Bestands: **Sozialversicherungsrecht**.

## Überblick raw/

| Ordner | Inhalt | Umfang |
|--------|--------|--------|
| `raw/LGVE 3. Abteilung/` | Publizierte Rechtsprechung der 3. Abteilung, nach Jahrgängen (1981–2025). **Index & Methode:** [[lgve-3-abteilung]] | 846 PDFs (Scans) |
| `raw/Literatur/` | Fachliteratur Sozialversicherungsrecht (IV, UVG, EL, Gutachten, Invaliditätsbemessung) | ~191 Dateien |
| `raw/Statistische Grundlagen/` | LSE-Tabellen (Lohnstrukturerhebung), Nominallohnindizes, betriebsübliche Arbeitszeit – für Invaliditätsgradberechnung. **Inventar:** [[statistische-grundlagen]] | – |
| `raw/TBS/` | Textbausteine (Urteilsentwurf), nach Gesetzesartikeln: ATSG21/22, IVG21/22, TB UVG. **Finder:** [[textbausteine]] | 5 DOCX |

## Hinweise zur Erschliessung

- **LGVE 3. Abteilung:** letzte Priorität. Diese Entscheide sind grundsätzlich über den **opencaselaw-MCP** erschliessbar (Sammlung `lu_gerichte`, LU; SVR-Entscheide über Aktenzeichen `5V…`/`S…` und Stichwortsuche), statt die 846 PDFs zu parsen. Eine vollständige 1:1-Abdeckung der publizierten LGVE-III-Reihe über opencaselaw ist allerdings nicht garantiert.
- **Literatur / TBS / Statistische Grundlagen:** vorrangig zu erschliessen; PDFs/DOCX werden lokal mit dem `liteparse`-Skill geparst.

## Wo finde ich was im Wiki?

Jede Wiki-Seite nennt im Frontmatter unter `location:` den zugehörigen `raw/`-Pfad. Der [[index]] listet alle Seiten nach Kategorie.
