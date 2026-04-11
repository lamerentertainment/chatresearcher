---
title: Berechnung Tagessatz - Formular für Geldstrafen
created: 2026-04-11
last_updated: 2026-04-11
source_count: 1
status: reviewed
location: raw/Formulare/Berechnungsformular Tagessatz D.xlsx
---

## Zusammenfassung

Das Berechnungsformular dient der Ermittlung des Tagessatzes für Geldstrafen gemäss Art. 34 StGB. Der Tagessatz basiert auf dem monatlichen Nettoeinkommen der verurteilten Person unter Berücksichtigung von Unterstützungsabzügen und Korrekturfaktoren. [Quelle: Berechnungsformular Tagessatz D.xlsx]

## Berechnungsstruktur

### 1. Monatseinkommen netto

**Ausgangswert:** Einkommen nach Abzug von AHV/IV/EO/PK

**Beispiel:** Fr. 6'250.00

### 2. Pauschalabzug

**Satz:** 20-30% (je nach Einkommen)
- Für Krankenkasse und Steuern
- **Beispiel (20%):** Fr. 6'250.00 → verbleibend Fr. 6'250.00 (Pauschalabzug bereits berücksichtigt)

### 3. Unterstützungsabzüge

| Berechtigte | Prozentsatz | Beispielbetrag |
|-------------|-------------|----------------|
| Ehepartner (nicht erwerbstätig) | 15% | Fr. 0.00 |
| 1. Kind | 15% | Fr. 0.00 |
| 2. Kind | 12.5% | Fr. 0.00 |
| 3. Kind (und weitere) | 10% | Fr. 0.00 |

### 4. Grundtagessatz

**Berechnung:** (Einkommen - Abzüge) / 30

**Beispiel:**
```
Zwischenresultat:       Fr. 6'250.00
Grundtagessatz:         Fr.   208.33 (6'250 / 30)
```

### 5. Zusatzfaktoren als Korrektiv

**Absolute Beträge** (zum Grundtagessatz addieren/subtrahieren):

| Faktor | Wirkung |
|--------|---------|
| Vermögen | Erhöhung (+) |
| Liegenschaften | Erhöhung (+) |
| Lebensaufwand | Erhöhung (+) |
| Schulden | Verminderung (-) |
| Ausbildungskosten | Verminderung (-) |
| Weitere Faktoren | Nach Ermessen |

### 6. Finaler Tagessatz

**Rundung:** Auf CHF 10 abgerundet

**Beispiel:**
```
Grundtagessatz:         Fr. 208.33
Korrekturfaktoren:      Fr.   0.00
Höhe des Tagessatzes:   Fr. 200.00 (auf CHF 10 abgerundet)
```

## Berechnung der Geldstrafe

**Formel:** Anzahl Tagessätze × Höhe des Tagessatzes

**Beispiel:**
```
Anzahl Tagessätze:      90
Höhe des Tagessatzes:   Fr. 200.00
Geldstrafe total:       Fr. 18'000.00
```

## Rechtliche Grundlage

**Art. 34 StGB - Geldstrafe:**
- Das Gericht bestimmt die Anzahl Tagessätze nach der Schuld des Täters/der Täterin
- Der Tagessatz bemisst sich nach den wirtschaftlichen Verhältnissen
- Mindestens 1, höchstens 360 Tagessätze
- Höchstbetrag: 3 Jahre Freiheitsstrafe als Ersatzfreiheitsstrafe

## Beispielrechnung

**Ausgangslage:**
- Monatseinkommen netto: Fr. 6'250.00
- Verheiratet, Ehepartner nicht erwerbstätig
- 2 Kinder
- Keine besonderen Vermögensverhältnisse

**Berechnung:**
```
Monatseinkommen:        Fr. 6'250.00
Pauschalabzug 20%:      Fr. 1'250.00
Zwischenresultat:       Fr. 5'000.00
Unterstützungsabzüge:   
  - Ehepartner 15%:     Fr.   750.00
  - 1. Kind 15%:        Fr.   750.00
  - 2. Kind 12.5%:      Fr.   625.00
Total Abzüge:           Fr. 2'125.00
Verfügbares Einkommen:  Fr. 2'875.00
Grundtagessatz:         Fr.    95.83 (2'875 / 30)
Tagessatz (gerundet):   Fr.    90.00
```

## Siehe auch

[[strafzumessung-art47-stgb]] - Strafzumessung nach Art. 47 StGB
[[strafzumessung-tabelle]] - Strafzumessungstabelle für mehrere Delikte
[[strafmassempfehlungen-svg]] - Strafmassempfehlungen für Strassenverkehrsdelikte
