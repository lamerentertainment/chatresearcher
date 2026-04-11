---
title: Berechnung ZMG-Kosten - Formular mit MWST 7.7% und 8%
created: 2026-04-11
last_updated: 2026-04-11
source_count: 2
status: reviewed
location: raw/Formulare/Berechnung ZMG Kosten 7.7 %.xlsx, raw/Formulare/Berechnung ZMG Kosten 8 %.xlsx
---

## Zusammenfassung

Die ZMG-Kostenrechner dienen der Berechnung von Honoraren und Auslagen für das Zwangsmassnahmengericht. Es existieren zwei Versionen: eine mit MWST 8% (älter) und eine mit MWST 7.7% (neu). [Quelle: Berechnung ZMG Kosten 7.7 %.xlsx, Berechnung ZMG Kosten 8 %.xlsx]

## Honorarbeträge (beide Versionen)

| Verfahren | Honorar 100% | Auslagen | Honorar 100% + Auslagen |
|-----------|-------------|----------|------------------------|
| KrG       | Fr. 342.70  | Fr. 7.80 | Fr. 350.50 |
| ZMG (1)   | Fr. 269.10  | Fr. 4.20 | Fr. 273.30 |
| ZMG (2)   | Fr. 266.80  | Fr. 4.20 | Fr. 271.00 |
| UV        | Fr. 3'406.30| Fr. 237.50| Fr. 3'643.80 |

## Berechnungsvarianten

### Honorar 100% (bei Obsiegen)

```
Honorar 100%:           Fr. 342.70 (KrG)
Auslagen:               Fr.   7.80
Honorar + Auslagen:     Fr. 350.50
MWST (8%):              Fr.  23.93
Total auszubezahlen:    Fr. 323.02
```

### Honorar 85% (bei Unterliegen)

```
Honorar 85%:            Fr. 291.30 (85% von 342.70)
Auslagen:               Fr.   7.80
Honorar + Auslagen:     Fr. 299.10
MWST (8%):              Fr.  23.93
Total auszubezahlen:    Fr. 323.02
```

### 15% des Honorars (Differenz)

```
15% des Honorars:       Fr.  51.41
MWST (8%):              Fr.   4.11
Total auszubezahlen:    Fr.  55.52
```

## MWST-Vergleich

| Position | MWST 8% | MWST 7.7% | Differenz |
|----------|---------|-----------|-----------|
| KrG Total (100%) | Fr. 23.93 | Fr. 23.03 | Fr. 0.90 |
| KrG Total (85%) | Fr. 23.93 | Fr. 23.03 | Fr. 0.90 |
| 15% Honorar | Fr. 4.11 | Fr. 3.96 | Fr. 0.15 |
| ZMG Total | Fr. 18.63 | Fr. 18.48 | Fr. 0.15 |
| UV Total | Fr. 250.63 | Fr. 241.67 | Fr. 8.96 |

## Beispiel: Komplette Berechnung (UV)

**Honorar 100%:**
```
Honorar 100%:           Fr. 3'406.30
Auslagen:               Fr.   237.50
Honorar + Auslagen:     Fr. 3'643.80
MWST 8%:                Fr.   250.63
Total auszubezahlen:    Fr. 3'383.48
```

**Honorar 85%:**
```
Honorar 85%:            Fr. 2'895.36
Auslagen:               Fr.   237.50
Honorar + Auslagen:     Fr. 3'132.86
MWST 8%:                Fr.   250.63
Total auszubezahlen:    Fr. 3'383.48
```

## Anwendungsbereiche

Das Formular enthält separate Berechnungsfelder für:
- **KrG** (Kriminalgericht)
- **ZMG** (Zwangsmassnahmengericht) - zwei Varianten
- **UV** (Untersuchungsverfahren)

## Rechtliche Grundlage

Die Honorarbemessung für das Zwangsmassnahmengericht richtet sich nach den kantonalen Richtlinien und der Kostenverordnung.

## Siehe auch

[[berechnung-anwaltshonorar]] - Allgemeine Anwaltshonorar-Berechnung
[[kostenrechner]] - Umfassender Kostenrechner für alle Verfahren
[[antrag-sicherheitshaft-zmg]] - Anträge an das ZMG
