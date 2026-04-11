---
title: Formulare - Übersicht der Berechnungsformulare und Tabellen
created: 2026-04-11
last_updated: 2026-04-11
source_count: 8
status: reviewed
location: raw/Formulare/
---

## Zusammenfassung

Diese Seite bietet eine Übersicht aller Berechnungsformulare und Tabellen im Ordner "Formulare". Die Formulare dienen der Berechnung von Anwaltshonoraren, ZMG-Kosten, Tagessätzen, Verfahrenskosten und der Anrechnung von Untersuchungshaft. [Quelle: Formulare/*.xlsx, *.xlsm, *.xls, *.url]

## Berechnungsformulare

### [[berechnung-anwaltshonorar]]
**Datei:** Berechnung Anwaltskosten ab 01.01.2018.xlsx

Berechnungsformular für Anwaltshonorare mit Unterscheidung nach:
- Honorar 100% (bei Obsiegen)
- Honorar 85% (bei Unterliegen)
- MWST 8% (bis 31.12.2017) bzw. 7.7% (ab 01.01.2018)
- Auslagen
- 15% des Honorars (bei certain Konstellationen)

Enthält Berechnungen für KrG, ZMG und UV.

### [[berechnung-zmg-kosten]]
**Dateien:** 
- Berechnung ZMG Kosten 7.7 %.xlsx
- Berechnung ZMG Kosten 8 %.xlsx

Zwei Versionen des ZMG-Kostenrechners mit unterschiedlichen MWST-Sätzen:
- **8% Version:** Honorar KrG Fr. 342.70, ZMG Fr. 269.10/266.80, UV Fr. 3'406.30
- **7.7% Version:** Gleiche Honorarbeträge, reduzierter MWST-Satz

Berechnung von:
- Honorar 100% + Auslagen
- Honorar 85% + Auslagen
- Total auszubezahlen inkl. MWST
- 15% des Honorars

### [[berechnung-tagessatz]]
**Datei:** Berechnungsformular Tagessatz D.xlsx

Berechnung des Tagessatzes für Geldstrafen gemäss StGB:
- **Grundlage:** Monatseinkommen netto (nach AHV/IV/EO/PK)
- **Pauschalabzug:** 20-30% (Krankenkasse, Steuern)
- **Unterstützungsabzüge:** 
  - Ehepartner (nicht erwerbstätig): 15%
  - 1. Kind: 15%
  - 2. Kind: 12.5%
  - 3. und weitere Kinder: 10%
- **Grundtagessatz:** Einkommen / 30
- **Korrekturfaktoren:** Vermögen, Liegenschaften, Lebensaufwand, Schulden, Ausbildungskosten
- **Rundung:** Auf CHF 10 abgerundet

### [[kostenrechner]]
**Datei:** Kostenrechner.xlsx (Version 1.2)

Umfassender Kostenrechner für Strafverfahren mit:
- **Verfahrenstypen:** Untersuchungsverfahren, Erstinstanz, ZMG, Berufung, Neubeurteilung
- **Honorar-Quoten:** 100% (Obsiegen), 85% (Unterliegen)
- **MWST-Sätze:** 8% und 7.7%
- **Kostenarten:** Honorar, Auslagen (mit/ohne MWST), Untersuchungskosten, Spruchgebühren
- **Verteilung:** Berechnung der Kostenanteile (Staat vs. beschuldigte Person)
- **Differenzberechnung:** Differenz zum vollen Honorar pro Verfahrensstufe

### [[strafzumessung-tabelle]]
**Datei:** Strafzumessung Tabelle.xlsm

Tabelle zur Strafzumessung bei mehreren Delikten:
- **Spalten:** Tatbestand, Schuldspruch, Deliktssumme, Tatverschulden, FS/GS-Einsatzstrafe
- **Beispiele:** Verkauf Porsche (Fr. 25'000), Fälschung Unterschrift, Zahlungen Garage, Misswirtschaft, Gläubigerschädigung, Gratifikation, Swisscom Rechnungen, Verkehrsbussen, Wertberichtigungen
- **Berechnung:** Asperationsatz FS/GS (0.33/0.25)
- **Total:** Tagessatz-Berechnung mit Asperation

### [[anrechnung-untersuchungshaft]]
**Datei:** Tabelle Anrechnung Untersuchungshaft.xls

Einfache Berechnung der Untersuchungshaft-Dauer:
- **Eingabe:** Tag des Beginns und Beendigung (Format: TTMMJJ)
- **Ausgabe:** Total Untersuchungshaft (Zählung der Nächte)
- **Beispiel:** 30.08.2007 - 05.09.2007 = 6 Nächte

## Externe Links

### [[betmg-strafzumessungsrechner]]
**Datei:** BetmG Strafzumessungsrechner.xlsx.url

**URL:** SharePoint Wissensmanagement KRG → Merkblätter Ordner

Strafzumessungsrechner für Betäubungsmittelgesetz-Verfahren (BetmG).

## Siehe auch

[[strafmassempfehlungen-svg]] - Strafmassempfehlungen für Strassenverkehrsdelikte
[[strafzumessung-art47-stgb]] - Strafzumessung nach Art. 47 StGB
[[berechnung-differenz-anwaltshonorar]] - Berechnung der Differenz zum vollen Anwaltshonorar
