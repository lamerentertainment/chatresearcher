---
title: Anrechnung Untersuchungshaft - Berechnungstabelle
created: 2026-04-11
last_updated: 2026-04-11
source_count: 1
status: reviewed
location: raw/Formulare/Tabelle Anrechnung Untersuchungshaft.xls
---

## Zusammenfassung

Die Tabelle dient der einfachen Berechnung der Dauer von Untersuchungshaft. Sie ermittelt automatisch die Anzahl Nächte zwischen dem Tag des Beginns und dem Tag der Beendigung der Untersuchungshaft. [Quelle: Tabelle Anrechnung Untersuchungshaft.xls]

## Funktionsweise

### Eingabefelder

| Feld | Format | Beschreibung |
|------|--------|-------------|
| Tag des Beginns | TTMMJJ | Startdatum der Untersuchungshaft |
| Tag der Beendigung | TTMMJJ | Enddatum der Untersuchungshaft |

### Ausgabe

| Feld | Beschreibung |
|------|-------------|
| Total Untersuchungshaft | Anzahl Nächte (Zählung der Nächte) |

## Berechnungsmethode

**Formel:** Anzahl Nächte = Enddatum - Beginndatum

**Beispiel:**
```
Tag des Beginns:      30.08.2007
Tag der Beendigung:   05.09.2007
Total Nächte:         6 Nächte
```

## Rechtliche Bedeutung

### Anrechnung auf Strafe

**Art. 64 StGB - Anrechnung der Untersuchungshaft:**
- Die Untersuchungshaft wird auf die Freiheitsstrafe angerechnet
- Anrechnung erfolgt tageweise
- Bei Geldstrafe: Umrechnung gemäss Art. 34 StGB

### Berechnung der Anrechnung

**Bei Freiheitsstrafe:**
```
Verhängte Freiheitsstrafe:    12 Monate
Untersuchungshaft:            6 Nächte
Verbleibende Strafe:          12 Monate - 6 Tage
```

**Bei Geldstrafe:**
```
Verhängte Geldstrafe:         90 Tagessätze à Fr. 200
Untersuchungshaft:            6 Nächte
Umrechnung:                   6 Tagessätze
Offene Geldstrafe:            84 Tagessätze × Fr. 200 = Fr. 16'800
```

## Praxisrelevanz

### Dispositiv-Formulierung

**Beispiel für ein Urteil:**
```
"Die Untersuchungshaft vom 30.08.2007 bis 05.09.2007 
wird auf die Freiheitsstrafe angerechnet."
```

### Besondere Konstellationen

**Mehrfache Untersuchungshaft:**
- Bei mehreren Haftperioden: Jede Periode separat berechnen
- Total aller Nächte für die Anrechnung summieren

**Unterbrochene Untersuchungshaft:**
- Haftunterbrüche (z.B. für Hospitalisation) werden nicht mitgezählt
- Nur tatsächliche Hafttage zählen

## Siehe auch

[[sicherheitshaft]] - Sicherheitshaft nach Art. 220-237 StPO
[[tabelle-anrechnung-untersuchungshaft]] - Übersicht zur Anrechnung von Untersuchungshaft
[[haftverlaengerung]] - Haftverlängerungsgesuche
