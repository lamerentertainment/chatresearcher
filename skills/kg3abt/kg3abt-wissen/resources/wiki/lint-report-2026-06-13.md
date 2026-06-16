---
title: Lint-Report 2026-06-13
created: 2026-06-13
last_updated: 2026-06-13
source_count: 0
status: reviewed
location: wiki/
---

Zweite Gesundheitsprüfung des Wikis nach den Cron-Ingest-Batches 18–31 (Stand: **78 Themenseiten**, 159/191 Literatur-PDFs erschlossen). Methodik wie beim [[lint-report-2026-06-12|ersten Lint]]: maschinelle Link-/Quellen-/Statusanalyse über alle `wiki/*.md` plus inhaltliche Stichproben. Schweregrade: 🔴 kritisch · 🟡 Warnung · 🔵 Info.

## Zusammenfassung

| Prüfpunkt | Ergebnis |
|-----------|----------|
| Kaputte/ins Leere zeigende Wiki-Links | **0** ✅ (1 False Positive im alten Report neutralisiert) |
| Verwaiste Seiten (keine eingehenden Links) | **0** ✅ |
| Seiten ohne jede Quellenangabe | **0** ✅ |
| Schwach verlinkt (genau 1 eingehender Link) | **0** ✅ |
| Widersprüche (markiert) | 6 Seiten (alle intentional) |
| Status `draft` | 1 (verfahrensfreie-verfuegung) |
| Status `reviewed` | 80 |

Das Wiki ist auch nach **+22 Seiten** seit dem letzten Lint strukturell **sehr gesund**: vollständige Verlinkung, durchgängige Quellen, keine Waisen, keine schwachen Knoten.

## 🔴 Kritisch

Keine.

## 🟡 Warnungen

Keine echten (sich ausschliessenden) Widersprüche. Die 6 `WIDERSPRUCH`-Seiten dokumentieren bewusste Rechts-/Praxisänderungen und nennen jeweils die massgebliche (neuere) Quelle: [[art-43a-atsg]], [[lse-tabellenlohn]], [[bge-148-v-174]], [[bger-8c-823-2023]], [[depression-invaliditaet]], [[abhaengigkeitserkrankungen]]. → Kein Handlungsbedarf.

## 🔵 Info / erledigte Lückenfüller

Seit dem letzten Lint abgearbeitet:

- ✅ **IV-Rundschreiben 339/334 (+ 298/328/355)** Volltext erschlossen → [[iv-rundschreiben-uebersicht]]; «noch nicht erschlossen»-Vermerk in [[iv-rundschreiben-339]] entfernt.
- ✅ **PTBS / Schreckereignis** → [[unfall-psyche-hirnverletzung]], [[uvg-kausalzusammenhang]].
- ✅ **BGE 143 V 418** (Ausweitung auf alle psychischen Leiden) → in [[bge-143-v-409]] und [[konsistenzpruefung]] ergänzt.

Offen / neu vorgemerkt:

- 🔵 **`BSV_Abklärungsprozess_IV.pdf`** (316 KB Prozesshandbuch) weiterhin zurückgestellt – verdient einen eigenen Durchgang.
- 🔵 **Draft:** [[verfahrensfreie-verfuegung]] bleibt Kurzeintrag.
- 🔵 **EGMR/EMRK-Cluster** (Kradolfer ZBl 2012, Dumermuth Juristentag 2014, Müller «(Schleich-)Wege zum Verwaltungsrechtsschutz», Pärli «Uber-Urteile») – Batch begonnen (extrahiert), aber zugunsten dieses Lints zurückgestellt; als nächster Ingest sinnvoll. Würde [[egmr-vukota-bojic]] / [[egmr-di-trizio]] um eine Übersicht «EGMR-Rechtsprechung zum Leistungsabbau» ergänzen.
- 🔵 **Verbleibend 32 offene PDFs** – überwiegend Einzelstücke/Randthemen (Medienartikel, SECO/EKAS-Berichte, Grundriss SVR, Rechtsprechungsübersichten Hürzeler/Biaggi).

## Konzepte, inline erwähnt – Ausbaupotenzial (kein Fehler)

*RAD (Regionaler Ärztlicher Dienst)*, *Mahn- und Bedenkzeitverfahren*, *ausserordentliche Bemessungsmethode*, *Wiedererwägung/prozessuale Revision (Art. 53 ATSG)*, *Statusfrage/Sperrfristenschutz (Art. 336c OR)*.

## Geprüfte Stichproben (Konsistenz)

- Neuere Leitentscheide konsistent eingebunden: **143 V 418** ([[bge-143-v-409]], [[konsistenzpruefung]]); **146 V 51** ([[koerperschaedigung-uvg]]); **148 V 49** ([[kritik-indikatorenpraxis-jeger]]); **8C_626/2024** ([[uv-pflegeleistungen]]); **1C_595/2023** ([[psychische-gesundheit-eingliederung]]). ✅
- Indikatoren-Kritik-Achse vollständig verlinkt: juristisch ([[kritik-schmerzrechtsprechung]], [[standardindikatoren]]/Egli-Slavik), medizinisch ([[kritik-indikatorenpraxis-jeger]]). ✅
- Begutachtungs-Cluster (≈13 Seiten) untereinander dicht vernetzt. ✅
