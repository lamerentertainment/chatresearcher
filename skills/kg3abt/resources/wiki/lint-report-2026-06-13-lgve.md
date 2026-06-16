---
title: Lint-Report 2026-06-13 (nach LGVE-Ingest)
created: 2026-06-13
last_updated: 2026-06-13
source_count: 0
status: reviewed
location: wiki/
---

Gesundheitsprüfung des Wikis nach Abschluss des LGVE-SVR-Ingests (13 Jahresseiten 2013–2025, 74 Entscheide). Geprüft: tote/fehlende Links, verwaiste Seiten, Status-Konsistenz, Quellenangaben, Frontmatter, Konzept-Lücken und Widersprüche. **Gesamtbefund: strukturell sehr gesund** – keine toten Wikilinks, keine verwaisten Seiten. Offene Punkte betreffen v. a. **fehlende Konzeptseiten** zu wiederkehrenden LGVE-Themen sowie zwei Status-Altlasten.

## Kennzahlen

- Inhaltsseiten (ohne index/log/lint): **101**
- Tote Wikilinks (`[[…]]` ohne Datei): **0** 🔵
- Verwaiste Seiten (kein eingehender Link): **0** 🔵
- Status: 102× `reviewed`, 1× `needs_update`, 1× `draft`

## 🔴 Kritisch

*Keine.* Keine inhaltlichen Widersprüche zwischen Seiten; keine fehlenden Kernseiten im SVR-Fokus. Der einzige strukturelle Widerspruch (LGVE-Band III ≤2012 ≠ SVR) ist in [[lgve-3-abteilung]] bereits ausdrücklich als `> WIDERSPRUCH` markiert und aufgelöst (Scope-Klärung).

## 🟡 Warnung

1. **Veralteter Status** [[lgve-3-abteilung]]: `status: needs_update` – stammt aus der Zeit vor dem Ingest. Der SVR-Bestand ist nun vollständig erschlossen und der Strukturbruch dokumentiert. → **In diesem Lint auf `reviewed` korrigiert.**
2. **`status: draft`** auf [[verfahrensfreie-verfuegung]]: einzige nicht abgeschlossene Inhaltsseite. Inhalt ist knapp; entweder ausbauen (Quelle/Beispiel) oder nach Review auf `reviewed` setzen.
3. **`source_count: 846`-Altlast (behoben):** Die frühere Formulierung «846 SVR-Entscheide 1981–2025» in [[lgve-3-abteilung]] war sachlich falsch (nur 2013–2025 III = SVR). Bereits in «846 PDF-Einträge» geändert und mit WIDERSPRUCH-Block erklärt.

## 🔵 Info / Lücken

1. **Konzept-Lücken** – mehrfach in LGVE-Jahresseiten referenzierte SVR-Themen ohne eigene Konzeptseite:
   - **Prämienverbilligung** (LU PVG/PVV, Art. 65 KVG) – belegt durch **LGVE 2016 III Nr. 7** und **2018 III Nr. 1/6/7** (4 Leitentscheide). Derzeit nur lose an [[kvg-wirtschaftlichkeitspruefung]] angebunden.
   - **Kinderrente / Ausbildungsbegriff** (Art. 25 Abs. 5 AHVG, Art. 49bis/49ter AHVV) – **LGVE 2018 III Nr. 2**, **2022 III Nr. 2**; in 5 Seiten erwähnt, keine eigene Seite.
   - **Assistenzbeitrag** (Art. 42quater ff. IVG) – **LGVE 2013 III Nr. 2**, **2023 III Nr. 3**; aktuell in [[hilflosenentschaedigung]] mitbehandelt, aber ohne eigene Seite.
   - **Erwerbsersatzordnung (EO/EOG)** inkl. Vaterschaftsentschädigung/Zivildienst – **LGVE 2022 III Nr. 1**, **2023 III Nr. 4**; keine eigene Seite.
   - **Militärversicherung (MVG)** – LGVE-Internetentscheid 2023 (5V 21 350); keine eigene Seite.
   - **Internationale SV-Koordination (FZA/VO 883/2004 / 1408/71)** – **LGVE 2013 III Nr. 6**, **2014 III Nr. 1**; derzeit in [[alv-koordination]] mitbehandelt.
2. **Meta-Seiten ohne `[Quelle:]`** – [[dateistruktur]] und [[literatur-ingest-status]] enthalten keine Quellenzitate. Akzeptabel (sie beschreiben die Ablage-/Ingest-Struktur selbst), daher nur Info.
3. **Pre-2013-Verwaltungsrecht** (LGVE Band III ≤2012: Bürger-, Ausländer-, Stimmrecht, Bildung, Bau, Sozialhilfe) ist **bewusst nicht** dokumentiert (ausserhalb SVR-Fokus). Offene Benutzerentscheidung, ob separat zu erfassen.

## Empfohlene neue Artikel (Top 3)

1. **`praemienverbilligung`** – KVG Art. 65 + LU Prämienverbilligungsgesetz/-verordnung; bündelt LGVE 2016 III Nr. 7 und 2018 III Nr. 1/6/7 (föderalistische Ausgestaltung, Einkommensgrenzen, keine nachträgliche Auszahlung, Aufrechnung Liegenschaftsunterhalt). Stärkste Lücke – vier einschlägige Leitentscheide.
2. **`kinderrente`** – Anspruch/Ausbildungsbegriff (Art. 25 Abs. 5 AHVG, Art. 49bis/49ter AHVV); LGVE 2018 III Nr. 2 (Stiefkind/Ausland), 2022 III Nr. 2 (Sprachaufenthalt), 2024 III Nr. 7 (Rückerstattung).
3. **`assistenzbeitrag`** – Art. 42quater ff. IVG; LGVE 2013 III Nr. 2 («eigener Haushalt», Art. 39b IVV) und 2023 III Nr. 3 (Konkubinatspartner als Assistenzperson); aus [[hilflosenentschaedigung]] herauslösen.

## Verwandte Seiten

[[lgve-3-abteilung]] · [[index]] · [[lint-report-2026-06-13-abschluss]]
