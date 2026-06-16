---
title: Statistische Grundlagen (Inventar)
created: 2026-06-13
last_updated: 2026-06-13
source_count: 0
status: reviewed
location: raw/Statistische Grundlagen/
---

Diese Seite ist ein **Inventar** des Ordners `raw/Statistische Grundlagen/` – sie erschliesst die Daten **nicht inhaltlich**, sondern sagt dem Benutzer, **welche statistischen Grundlagen vorhanden sind und wo er sie findet**. Diese Tabellen werden für die Berechnung des [[invalideneinkommen|Invaliditätsgrads]] benötigt (LSE-Tabellenlöhne, Nominallohnindex zur Anpassung der Vergleichseinkommen). Funktionale Erläuterungen zu den Tabellentypen siehe [[lse-tabellenlohn]]. [Quelle: raw/Statistische Grundlagen/ (Verzeichnislisting)]

## Ordnerstruktur (Überblick)

```
raw/Statistische Grundlagen/
├── Betriebsübliche Arbeitszeit nach Wirtschaftsabteilungen (NOGA 2008) … .xlsx
├── Lohnstrukturerhebung/        (LSE-PDFs, LSE-Excel-Tabellen, Nominallohnindizes)
└── Nominallohnindex/            (Nominallohnindex je Basisjahr)
```

## 1. Lohnstrukturerhebung (LSE) — `Lohnstrukturerhebung/`

Die LSE des Bundesamts für Statistik (BFS) ist die Datengrundlage für das statistische [[invalideneinkommen]]. Die Tabellen (insb. **TA1**/**T1** Kompetenzniveau, **T17** nach beruflicher Stellung) sind die in der Praxis massgeblichen Werte – vgl. [[lse-tabellenlohn]].

### LSE-Gesamtpublikationen (PDF)

| Datei | Inhalt |
|-------|--------|
| `LSE 2004.pdf` · `LSE 2006.pdf` · `LSE 2008.pdf` · `LSE 2010.pdf` · `LSE 2012.pdf` | Vollpublikationen der jeweiligen Erhebung |
| `IV-Rundschreiben_Nr._328.pdf` | BSV-Weisung zur Anwendung der **LSE 2012** in der IV (vgl. [[iv-rundschreiben-uebersicht]]) |

### LSE-Tabellen (Excel) nach Tabellentyp

| Tabellentyp | Verfügbare Jahrgänge (Dateien) | Bedeutung |
|-------------|--------------------------------|-----------|
| **TA1_tirage_skill_level** | 2014, 2016, 2018, 2020, 2022, 2024 | Standardtabelle (privater Sektor) nach Kompetenzniveau – Hauptgrundlage Invalideneinkommen |
| **T1_tirage_skill_level** | 2018, 2020, 2022 | privater **und** öffentlicher Sektor, nach Kompetenzniveau |
| **T1b** | 2014, 2016 | Variante (älteres Format) |
| **T17** | `T17 (2012 bis 2020).xlsx`, `T17 (2012 bis 2022).xlsx` | nach **beruflicher Stellung** – gilt als realitätsnäher |
| **T18** | `LSE 2022 T18 Lohn nach Beschäftigungsgrad.xlsx` | Lohn nach **Beschäftigungsgrad** (Teilzeit) |
| **TA12** | `TA12 (2008 bis 2020).xlsx` | (Zeitreihe) |
| **T7** | `T7 (2006 bis 2010).xls` | (Zeitreihe) |

### Nominallohnindizes (im LSE-Ordner abgelegt)

`Nominallohnindex Basis 1993 (bis 2024).xlsx` · `… Basis 2010 (bis 2024).xlsx` · `… Basis 2015 (bis 2024).xlsx` · `… Basis 2020 (bis 2024).xlsx`

## 2. Nominallohnindex — `Nominallohnindex/`

`Nominallohnindex 1993.xlsx` · `Nominallohnindex 2010.xlsx` · `Nominallohnindex 2015.xlsx` · `Nominallohnindex 2020.xlsx`

Dient der **Anpassung der Vergleichseinkommen an die Lohnentwicklung** (Indexierung auf den massgeblichen Zeitpunkt; vgl. die Quartalsschätzungen-Thematik in [[invalideneinkommen]]).

## 3. Betriebsübliche Arbeitszeit (Wurzelordner)

`Betriebsübliche Arbeitszeit nach Wirtschaftsabteilungen (NOGA 2008), in Stunden pro Woche.xlsx` – nötig, um LSE-Monatslöhne (Basis 40 Std./Woche) auf die **betriebsübliche Wochenarbeitszeit** der jeweiligen Branche umzurechnen.

## Hinweis

Die LSE-Werte und ihre Anwendung sind in der bundesgerichtlichen Praxis umstritten (vgl. [[bge-148-v-174]], [[bger-8c-823-2023]], [[leidensbedingter-abzug]]). Diese Inventar-Seite verweist nur auf die **Datenablage**; die rechtliche Würdigung steht auf den genannten Themenseiten.

## Verwandte Seiten

[[lse-tabellenlohn]] · [[invalideneinkommen]] · [[dateistruktur]] · [[iv-rundschreiben-uebersicht]]

## Quellen

- raw/Statistische Grundlagen/ (Verzeichnisinventar, Stand 2026-06-13)
