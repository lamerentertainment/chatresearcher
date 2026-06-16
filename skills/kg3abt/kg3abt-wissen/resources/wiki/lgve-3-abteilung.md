---
title: LGVE 3. Abteilung – Übersicht, Index und Erschliessungsmethode
created: 2026-06-13
last_updated: 2026-06-13
source_count: 846
status: reviewed
location: raw/LGVE 3. Abteilung/
---

Die **LGVE 3. Abteilung** sind die in den Luzerner Gerichts- und Verwaltungsentscheiden publizierten Leitentscheide der **3. Abteilung des Kantonsgerichts Luzern** (Sozialversicherungsrecht). Der Bestand in `raw/LGVE 3. Abteilung/` umfasst **846 PDF-Einträge (1981–2025)**, nach Jahrgängen abgelegt; Zitierform: **`LGVE [Jahr] III Nr. [N]`**. Diese Seite ist der **Einstieg**: Sie hält den vollständigen Index fest und beschreibt, wie der Inhalt eines Entscheids über den `opencaselaw`-MCP abgerufen wird. [Quelle: raw/LGVE 3. Abteilung/ (Verzeichnisinventar)]

> **WICHTIG – Strukturbruch 2012/2013 (entdeckt 2026-06-13):** Nur die Jahrgänge **2013 III – 2025 III** sind **sozialversicherungsrechtlich** (= die per 1.6.2013 gebildete 3. Abteilung des Kantonsgerichts). Die im selben raw-Ordner liegenden Einträge **bis und mit 2012 III** stammen aus der **alten LGVE-Systematik**, in der „Band III" das **allgemeine Verwaltungsrecht** bezeichnete (Bürgerrecht/Einbürgerung, Ausländerrecht, Stimm-/Volksrechte, Bildung, Planungs- und Baurecht, Sozialhilfe) – entschieden von **Regierungsrat/Departementen/Verwaltungsgericht**, **nicht** von einer SV-Abteilung.
>
> WIDERSPRUCH: «846 SVR-Entscheide 1981–2025» (frühere Annahme bei Index-Erstellung) vs. **tatsächlich nur 2013–2025 III = SVR** (≈ 60 Entscheide); ≤2012 III = Verwaltungsrecht, **out of scope** für dieses SVR-Wiki. [Quelle: raw/LGVE 3. Abteilung/2012/ Nr. 1–21 (Entscheidköpfe)]
>
> Das **vor 2013 publizierte Sozialversicherungsrecht** stand in der alten LGVE-Systematik im **Band II** (z. B. «S 98 624 = LGVE 1999 **II** Nr. 46», Arbeitslosenversicherung) – diese Bände sind **nicht** Teil des raw-Ordners. [Quelle: opencaselaw lu_gerichte (Stichprobe alte S-Aktenzeichen)]

## Wichtiger Status / Erschliessungsmethode

- Die raw-PDFs sind **gescannte Bilder ohne Textebene** (`pdftotext` liefert nichts) – ihr Inhalt ist nur per OCR **oder** über `opencaselaw` zugänglich.
- **Strategie (vgl. [[dateistruktur]]):** Inhalt **nicht** durch OCR der 846 Scans, sondern über den **`opencaselaw`-MCP** (Sammlung `lu_gerichte`). Dort sind LU-SVR-Entscheide über **Stichwortsuche**, **LGVE-Zitat** oder **Aktenzeichen** (`5V…` / `S…`) erschliessbar. Beispiel-Aktenzeichen aus dem Bestand: **5V 21 350** (= «Internetentscheid» 2023).
- ✅ **Update 2026-06-13:** Der `opencaselaw`-MCP (Sammlung `lu_gerichte`) ist **erreichbar**; der inhaltliche Ingest läuft jahrgangsweise rückwärts ab 2025. Erschlossene Jahrgänge siehe Abschnitt «Inhaltlich erschlossene Jahrgänge» unten.

## Workflow für den inhaltlichen Ingest (sobald opencaselaw verfügbar)

Pro Entscheid:
1. In opencaselaw suchen: `search_decisions` (canton/Gericht LU, `legal_area` Sozialversicherung) per Stichwort/Jahr, **oder** `get_decision` per Aktenzeichen, **oder** Volltextsuche nach «LGVE [Jahr] III Nr. [N]».
2. **Regeste** und **kanonische URL** (`canonical_url` / `markdown_link`) übernehmen.
3. Kurze Themenzuordnung + Verlinkung zu den bestehenden Konzeptseiten (z. B. [[invalideneinkommen]], [[strukturiertes-beweisverfahren]], [[uvg-kausalzusammenhang]] …).
4. Eintrag auf einer Jahres-Themenseite ablegen, mit dem **opencaselaw-Link**, damit der Volltext jederzeit (auch ohne `raw/`) abrufbar bleibt.

Dies eignet sich als **`/loop`-Aufgabe** (jahrgangs- oder themenweise Batches).

## Vollständiger Index (846 Entscheide)

Format: Jahr (Anzahl) – Nummern. Soweit nicht anders vermerkt, sind die Nummern **lückenlos 1…N**.

| Jahr | Anz. | Nummern / Bemerkung |
|------|------|---------------------|
| 1981 | 31 | Nr. 1–31 |
| 1982 | 39 | Nr. 1–39 |
| 1983 | 37 | Nr. 1–37 |
| 1984 | 57 | Nr. 1–57 |
| 1985 | 47 | Nr. 1–47 |
| 1986 | 44 | Nr. 1–44 |
| 1987 | 48 | Nr. 1–48 |
| 1988 | 28 | Nr. 1–28 |
| 1989 | 29 | Nr. 1–29 |
| 1990 | 21 | Nr. 1–21 |
| 1991 | 23 | Nr. 1–23 |
| 1992 | 21 | Nr. 1–21 |
| 1993 | 27 | Nr. 1–27 |
| 1994 | 17 | Nr. 1–17 |
| 1995 | 13 | Nr. 1–13 |
| 1996 | 15 | Nr. 1–15 |
| 1997 | 16 | Nr. 1–16 |
| 1998 | 11 | Nr. 1–11 |
| 1999 | 16 | Nr. 1–16 |
| 2000 | 17 | Nr. 1–17 |
| 2001 | 19 | Nr. 1–19 |
| 2002 | 15 | Nr. 1–15 |
| 2003 | 21 | Nr. 1–21 |
| 2004 | 21 | Nr. 1–21 |
| 2005 | 20 | Nr. 1–20 |
| 2006 | 18 | Nr. 1–18 |
| 2007 | 15 | Nr. 1–15 |
| 2008 | 19 | Nr. 1–19 |
| 2009 | 14 | Nr. 1–14 |
| 2010 | 15 | Nr. 1–15 |
| 2011 | 16 | Nr. 1–16 |
| 2012 | 19 | Nr. 1–21 **ohne Nr. 4 und Nr. 12** |
| 2013 | 6 | Nr. 1–6 |
| 2014 | 5 | Nr. 1–5 |
| 2015 | 4 | Nr. 1–4 |
| 2016 | 9 | Nr. 1–9 |
| 2017 | 5 | Nr. 1–5 |
| 2018 | 7 | Nr. 1–7 |
| 2019 | 1 | Nr. 1 |
| 2020 | 5 | Nr. 1–5 |
| 2021 | 5 | Nr. 1–5 |
| 2022 | 3 | Nr. 1–3 |
| 2023 | 8 | Nr. 1–7 + «Internetentscheid **5V 21 350**» |
| 2024 | 12 | Nr. 1–11 (Nr. 4 doppelt abgelegt) |
| 2025 | 7 | Nr. 1–6 + «Internetentscheid» |

**Beobachtung:** Bis ~2011 wurden pro Jahr 15–57 Entscheide publiziert, danach deutlich weniger (1–12/Jahr) – die jüngeren Jahrgänge sind für die aktuelle Praxis am relevantesten und sollten beim inhaltlichen Ingest **priorisiert** werden (2020–2025 zuerst, dann rückwärts).

## Inhaltlich erschlossene Jahrgänge

Pro erschlossenem Jahrgang besteht eine eigene Jahres-Themenseite mit Regeste + opencaselaw-Link je Entscheid:

- **2025** → [[lgve-2025-iii]] (6 nummerierte Leitentscheide + 1 Internetentscheid; opencaselaw `lu_gerichte` verfügbar) [Quelle: opencaselaw lu_gerichte]
- **2024** → [[lgve-2024-iii]] (11 nummerierte Leitentscheide Nr. 1–11; Schwerpunkte: IV-Rückforderung/Verwirkung, WEIV-Begutachtung, KVG, ME/CFS) [Quelle: opencaselaw lu_gerichte]
- **2023** → [[lgve-2023-iii]] (7 nummerierte Leitentscheide + 1 Internetentscheid; breit: Säule 3a, EO/Zivildienst, Assistenzbeitrag, UVG-Überentschädigung, Witwerrente/EGMR Beeler, Militärversicherung) [Quelle: opencaselaw lu_gerichte]
- **2022** → [[lgve-2022-iii]] (3 nummerierte Leitentscheide; EO/Vaterschaftsentschädigung, Kinderrente/Ausbildung, ALV-Beitragsbefreiung) [Quelle: opencaselaw lu_gerichte]
- **2021** → [[lgve-2021-iii]] (5 nummerierte Leitentscheide; AHV-Beitragsrecht, ALV/Corona-Kurzarbeit + Rückforderung, KVG-Pflegerestkosten) [Quelle: opencaselaw lu_gerichte]
- **2020** → [[lgve-2020-iii]] (5 nummerierte Leitentscheide; AHV-Beitragsrecht inkl. Art. 52 AHVG, ALV/Art. 40b AVIV, EL-Normenkontrolle Pflegetaxe) [Quelle: opencaselaw lu_gerichte]
- **2019** → [[lgve-2019-iii]] (1 Leitentscheid; IV-Invaliditätsbemessung: Homeoffice/ausgeglichener Arbeitsmarkt, Einkommensvergleich Teilerwerbstätige) [Quelle: opencaselaw lu_gerichte]
- **2018** → [[lgve-2018-iii]] (7 nummerierte Leitentscheide; Prämienverbilligung, Valideneinkommen, AHV-Beitragsstatus, Kinderrente, UVG-Integritätsschaden) [Quelle: opencaselaw lu_gerichte]
- **2017** → [[lgve-2017-iii]] (5 nummerierte Leitentscheide; Weisungs-/Verordnungskontrolle TARMED/KSIH/WML, AHV-Mitarbeiteraktien, KVG-Pflegerestkosten) [Quelle: opencaselaw lu_gerichte]
- **2016** → [[lgve-2016-iii]] (9 nummerierte Leitentscheide; KVG, IV-Begutachtung MEDAS/RAD, HE betreutes Wohnen, SchlB-Eingliederung, Prämienverbilligung, Verfahrenskosten) [Quelle: opencaselaw lu_gerichte]
- **2015** → [[lgve-2015-iii]] (4 nummerierte Leitentscheide, alle IV; Rentenrevision/Rentenbeginn, Depression/Therapieresistenz, altrechtliche Gutachten & BGE 141 V 281) [Quelle: opencaselaw lu_gerichte]
- **2014** → [[lgve-2014-iii]] (5 nummerierte Leitentscheide; ALV/FZA-Koordination, Vergleich Art. 50 ATSG, KVG-Hausarztmodell, unentgeltliche Verbeiständung, Resterwerbsfähigkeit/Alter) [Quelle: opencaselaw lu_gerichte]
- **2013** → [[lgve-2013-iii]] (6 nummerierte Leitentscheide; UVG-Ersatzprämie, Assistenzbeitrag, prozessuale Revision, PTBS, Pflege-Restfinanzierung, ALV-Leistungsexport; Übergang Verwaltungsgericht → KG) **← früheste SVR-Jahresseite (Untergrenze des SVR-Bestands)**

### ✅ SVR-Bestand vollständig erschlossen (2013–2025)

Damit sind **alle sozialversicherungsrechtlichen** LGVE-III-Jahrgänge erschlossen: **13 Jahresseiten 2013–2025 mit zusammen 74 Entscheiden**, je mit Regeste, Aktenzeichen, Datum und opencaselaw-Link.

**≤2012 III = ausserhalb des SVR-Fokus** (allgemeines Verwaltungsrecht, siehe Strukturbruch-Hinweis oben). Diese Jahrgänge werden **nicht** als SVR-Jahresseiten angelegt. Über das weitere Vorgehen (Verwaltungsrecht dennoch dokumentieren? oder LGVE-Ingest hier abschliessen?) entscheidet der Benutzer.

## Verwandte Seiten

[[dateistruktur]] · [[statistische-grundlagen]] · [[textbausteine]]

## Quellen

- raw/LGVE 3. Abteilung/ (Verzeichnisinventar, Stand 2026-06-13)
- opencaselaw-MCP, Sammlung `lu_gerichte` (für den künftigen inhaltlichen Abruf)
