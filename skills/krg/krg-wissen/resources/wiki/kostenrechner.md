---
title: Kostenrechner - Umfassender Rechner für Strafverfahren
created: 2026-04-11
last_updated: 2026-04-11
source_count: 1
status: reviewed
location: raw/Formulare/Kostenrechner.xlsx
---

## Zusammenfassung

Der Kostenrechner (Version 1.2) ist ein umfassendes Excel-Tool zur Berechnung aller Kosten in Strafverfahren. Er deckt alle Verfahrensstufen ab und berechnet sowohl die Verteidigungskosten als auch die Verfahrenskosten. [Quelle: Kostenrechner.xlsx]

## Funktionen

### Verfahrenstypen

Der Kostenrechner unterstützt folgende Verfahren:
1. **Untersuchungsverfahren** (UV)
2. **Erstinstanzliches Verfahren** (KrG)
3. **Verfahren vor Zwangsmassnahmengericht** (ZMG)
4. **Berufungsverfahren**
5. **Neubeurteilungsverfahren**

### Honorar-Quoten

| Situation | Quote |
|-----------|-------|
| Obsiegen | 100% |
| Unterliegen | 85% |

### MWST-Sätze

| Satz | Anwendung |
|------|-----------|
| 8.0% | Ältere Berechnungen (bis 31.12.2017) |
| 7.7% | Neuere Berechnungen (ab 01.01.2018) |

## Berechnungsstruktur

### Kostennote der Verteidigung

Für jedes Verfahren werden berechnet:

**Honorar:**
- Honorar mit 8% MWST
- Honorar mit 7.7% MWST

**Auslagen:**
- Auslagen mit 8% MWST
- Auslagen mit 7.7% MWST
- Auslagen ohne MWST

**Total:** Summe Honorar + Auslagen + MWST

### Verfahrenskosten

**Kostenarten:**
- Untersuchungskosten
- Spruchgebühr
- Weitere Auslagen
- Nicht verrechenbare Auslagen

**Verteilung:**
- Quote zulasten des Staates (%)
- Quote zulasten der beschuldigten Person (%)

## Verteilung der Kosten

### Verteidigungskosten

Der Rechner berechnet zwei Szenarien:

**1. 100% der Kostennote zu 85% entschädigt:**
```
Honorar (8% MWST):      Fr. [Betrag]
Honorar (7.7% MWST):    Fr. [Betrag]
Auslagen (8% MWST):     Fr. [Betrag]
Auslagen (7.7% MWST):   Fr. [Betrag]
Auslagen (ohne MWST):   Fr. [Betrag]
MWST (8%):              Fr. [Betrag]
MWST (7.7%):            Fr. [Betrag]
Total:                  Fr. [Betrag]
```

**2. 0% der Kostennote zu 100% entschädigt:**
(Gleiche Struktur wie oben)

### Gesamtkostennote pro Verfahren

**Zusammensetzung:**
```
Honorar (8% MWST):      Fr. [Betrag]
Honorar (7.7% MWST):    Fr. [Betrag]
Auslagen (8% MWST):     Fr. [Betrag]
Auslagen (7.7% MWST):   Fr. [Betrag]
Auslagen (ohne MWST):   Fr. [Betrag]
MWST (8%):              Fr. [Betrag]
MWST (7.7%):            Fr. [Betrag]
Total Kostennote:       Fr. [Betrag]
```

## Ergebnisberechnung

### Verteidigungskosten

| Position | Beschreibung |
|----------|-------------|
| Entschädigungsanspruch insgesamt | Total Honorar + Auslagen |
| Entschädigungsanspruch durch Staat | Staatlicher Anteil |
| Bereits ausbezahlte Entschädigung | Vorschüsse |
| Differenz zum vollen Honorar (UV) | Nachzahlung Untersuchungsverfahren |
| Differenz zum vollen Honorar (1. Instanz) | Nachzahlung Erstinstanz |
| Differenz zum vollen Honorar (ZMG) | Nachzahlung ZMG |
| Differenz zum vollen Honorar (Berufung) | Nachzahlung Berufung |
| Differenz zum vollen Honorar (Neubeurteilung) | Nachzahlung Neubeurteilung |
| Auszuzahlender Betrag | Finaler Anspruch |
| Rückerstattungsanspruch (Art. 135 Abs. 4 lit. a StPO) | Gegen beschuldigte Person |
| Entschädigungsanspruch (Art. 135 Abs. 4 lit. b StPO) | Gegen beschuldigte Person |

### Verfahrenskosten

| Position | Beschreibung |
|----------|-------------|
| Verfahrenskosten (ohne Berufung) | Total UV + 1. Instanz + ZMG |
| Verfahrenskosten Berufungsverfahren | Separate Berechnung |
| Verfahrenskosten zulasten beschuldigte Person | Anteil Beschuldigte |
| Verfahrenskosten zulasten Staat | Anteil Staat |

## Rechtliche Grundlagen

**Art. 135 Abs. 4 StPO - Kostenverteilung:**
- **lit. a:** Rückerstattungsanspruch des Kantons gegenüber der beschuldigten Person
- **lit. b:** Entschädigungsanspruch der Verteidigung gegenüber der beschuldigten Person

## Anwendungsbeispiel

**Untersuchungsverfahren:**
```
Honorar 100%:           Fr. 3'406.30
Auslagen:               Fr.   237.50
MWST 7.7%:              Fr.   250.63
Total Kostennote:       Fr. 3'894.43

Quote zulasten Staat:   100%
Quote zulasten Besch.:  0%

Staat zahlt:            Fr. 3'894.43
Beschuldigte zahlt:     Fr.     0.00
```

## Siehe auch

[[berechnung-anwaltshonorar]] - Einfache Anwaltshonorar-Berechnung
[[berechnung-zmg-kosten]] - Spezifische ZMG-Kostenberechnung
[[berechnung-differenz-anwaltshonorar]] - Differenzberechnung zum vollen Honorar
[[kostentragung-ohg]] - Kostentragung gemäss OHG
