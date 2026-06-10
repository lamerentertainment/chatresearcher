---
title: Strafzumessungstabelle - Berechnung bei mehreren Delikten
created: 2026-04-11
last_updated: 2026-04-11
source_count: 1
status: reviewed
location: raw/Formulare/Strafzumessung Tabelle.xlsm
---

## Zusammenfassung

Die Strafzumessungstabelle dient der systematischen Berechnung von Strafen bei mehreren Delikten. Sie ermöglicht die Erfassung aller Tatbestände mit Schuldspruch, Deliktssumme, Tatverschulden und der entsprechenden Einsatzstrafe in Tagessätzen. [Quelle: Strafzumessung Tabelle.xlsm]

## Tabellenstruktur

### Spalten

| Spalte | Beschreibung |
|--------|-------------|
| Tatbestand | Konkrete Deliktsbezeichnung mit Artikel |
| Schuldspruch | JA/NEIN |
| Erwägungen, Deliktssumme etc. | Geldbetrag oder qualitative Beschreibung |
| Tatverschulden | leicht / nicht mehr leicht / gering / dreist |
| FS Einsatzstrafe | Freiheitsstrafe in Monaten/Tagessätzen |
| GS Einsatzstrafe | Geldstrafe in Tagessätzen |

## Deliktskategorien (Beispiele)

### Vermögensdelikte StGB

| Artikel | Delikt | Beispielbetrag |
|---------|--------|----------------|
| Art. 158 StGB | Ungetreue Geschäftsbesorgung | Fr. 25'000 (Porsche) |
| Art. 164 StGB | Gläubigerschädigung | Fr. 50'000 (Gratifikation) |
| Art. 165 StGB | Misswirtschaft | Fr. 291'697 (Wertberichtigungen) |
| Art. 166 StGB | Unterlassen der Buchführung | 2 Monate ohne Betrieb |
| Art. 251 StGB | Urkundenfälschung | Fr. 18'000 (Unterschrift) |

### Weitere Delikte

| Artikel | Delikt | Beispielbetrag |
|---------|--------|----------------|
| Art. 253 StGB | Betrug | Fr. 2'583 (Kaufpreisangabe) |
| § 225 StG | Kantonales Steuergesetz | Fr. 2'583 |

## Tatverschulden-Kategorien

| Kategorie | Beschreibung | Typische Tagessätze |
|-----------|-------------|---------------------|
| gering | Bagatellbereich | 10-20 TS |
| leicht | Standardfälle | 30-90 TS |
| nicht mehr leicht | Erschwert | 120-150 TS |
| dreist | Besonders erschwert | 40+ TS |

## Berechnungsbeispiele aus der Tabelle

### Beispiel 1: Ungetreue Geschäftsbesorgung (Art. 158 StGB)

| Tatbestand | Schuldspruch | Summe | Verschulden | FS | GS |
|------------|-------------|-------|-------------|-----|-----|
| Verkauf Porsche Carrera | JA | Fr. 25'000 | leicht | 90 TS | 22.50 TS |
| Zahlung Garage Reichlin | JA | Fr. 18'000 | leicht | 80 TS | 20.00 TS |
| Gratifikation | JA | Fr. 50'000 | nicht mehr leicht | 120 TS | 30.00 TS |
| Zahlung Kontomed | JA | Fr. 2'625 | gering | 15 TS | 3.75 TS |
| Swisscom Rechnungen | JA | Fr. 816.73 | gering | 10 TS | 2.50 TS |
| Verkehrsbussen | JA | Fr. 1'290 | gering | 10 TS | 2.50 TS |
| Wertberichtigungen CDS | JA | Fr. 291'697 | nicht mehr leicht | 150 TS | 150.00 TS |
| Steintrennmaschine | JA | Fr. 3'071 | leicht | 40 TS | 10.00 TS |

### Beispiel 2: Urkundenfälschung (Art. 251 StGB)

| Tatbestand | Schuldspruch | Summe | Verschulden | FS | GS |
|------------|-------------|-------|-------------|-----|-----|
| Fälschung Unterschrift | JA | - | leicht | 30 TS | 7.50 TS |

### Beispiel 3: Misswirtschaft (Art. 165 StGB)

| Tatbestand | Schuldspruch | Summe | Verschulden | FS | GS |
|------------|-------------|-------|-------------|-----|-----|
| Misswirtschaft CDS | JA | - | leicht, Besorgniszeitpunkt früh klar | 90 TS | 22.50 TS |

### Beispiel 4: Gläubigerschädigung (Art. 164 StGB)

| Tatbestand | Schuldspruch | Summe | Verschulden | FS | GS |
|------------|-------------|-------|-------------|-----|-----|
| Gläubigerschädigung CDS | NEIN | Fr. 291'697 | nicht mehr leicht | - | - |

## Asperationsberechnung

**Asperationsatz:**
- **Freiheitsstrafe:** 0.33 (1/3)
- **Geldstrafe:** 0.25 (1/4)

**Berechnung:**
```
Total Einsatzstrafen FS:     1150 TS
Asperation (0.33):           358.75 TS
Total FS nach Asperation:    359 TS (ca. 12 Monate)

Total Einsatzstrafen GS:     359 TS
Asperation (0.25):           [berechnet]
Total GS nach Asperation:    [Endbetrag]
```

## Täterkomponente

| Faktor | Wert |
|--------|------|
| Widerrufene Freiheitsstrafe | nein |
| Asperierte Freiheitsstrafe | nein |

## Anwendung in der Praxis

**Schritt 1:** Alle Tatbestände erfassen mit:
- Artikelnummer
- Schuldspruch (JA/NEIN)
- Deliktssumme (falls zutreffend)
- Tatverschulden-Kategorie

**Schritt 2:** Einsatzstrafen bestimmen gemäss:
- Schwere des Delikts
- Deliktssumme
- Vorbelastung

**Schritt 3:** Asperation berechnen:
- Höchste Strafe als Basis
- Zuschlag für Konkurrenzdelikte

**Schritt 4:** Täterkomponente berücksichtigen:
- Vorstrafen
- Geständnis
- Wiedergutmachung

## Rechtliche Grundlage

**Art. 47 StGB - Strafzumessung:**
- Das Gericht misst die Strafe nach der Schuld zu
- Berücksichtigt Vorleben, persönliche Verhältnisse
- Bei mehreren Delikten: Asperation (Art. 49 StGB)

## Siehe auch

[[strafzumessung-art47-stgb]] - Strafzumessung nach Art. 47 StGB
[[berechnung-tagessatz]] - Berechnung des Tagessatzes für Geldstrafen
[[strafmassempfehlungen-svg]] - Strafmassempfehlungen für Strassenverkehrsdelikte
