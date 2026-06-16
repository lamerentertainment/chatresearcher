---
title: Lint-Report 2026-06-13 (Abschluss)
created: 2026-06-13
last_updated: 2026-06-13
source_count: 0
status: reviewed
location: wiki/
---

Abschliessende Gesundheitsprüfung nach **vollständigem Literatur-Ingest** (191/191 PDFs erledigt, 83 Themenseiten). Durchgeführt nach dem Stopp des Ingest-Loops (Cron `2a00601d` gelöscht). Methodik wie zuvor ([[lint-report-2026-06-12]], [[lint-report-2026-06-13]]): maschinelle Link-/Quellen-/Statusanalyse plus inhaltliche Stichproben. Schweregrade: 🔴 kritisch · 🟡 Warnung · 🔵 Info.

## Zusammenfassung

| Prüfpunkt | Ergebnis |
|-----------|----------|
| Kaputte/ins Leere zeigende Wiki-Links | **0** ✅ |
| Verwaiste Seiten (keine eingehenden Links) | **0** ✅ |
| Seiten ohne jede Quellenangabe | **0** ✅ |
| Schwach verlinkt (genau 1 eingehender Link) | **0** ✅ |
| Widersprüche (markiert) | 6 Seiten (alle intentional) |
| Status `draft` | 1 (verfahrensfreie-verfuegung) |
| Status `reviewed` | 86 |

Das Wiki ist nach Abschluss des Ingests **vollständig gesund**: lückenlose Verlinkung, durchgängige Quellen, keine Waisen, keine schwachen Knoten.

## 🔴 Kritisch / 🟡 Warnungen

Keine. Die 6 `WIDERSPRUCH`-Seiten ([[art-43a-atsg]], [[lse-tabellenlohn]], [[bge-148-v-174]], [[bger-8c-823-2023]], [[depression-invaliditaet]], [[abhaengigkeitserkrankungen]]) dokumentieren bewusste Rechts-/Praxisänderungen mit Nennung der jeweils massgeblichen neueren Quelle.

## 🔵 Info

- **Ingest abgeschlossen:** Alle 191 Literatur-PDFs sind abgehakt. Nicht als eigene Seite ausgearbeitete Einträge (Dubletten, Verwaltungs-/Aufsichts-/Medien-/Off-core-Dokumente) sind im [[literatur-ingest-status]] transparent als solche vermerkt – kein Eintrag wurde mit erfundenem Inhalt „erschlossen".
- **Draft:** [[verfahrensfreie-verfuegung]] bleibt bewusst Kurzeintrag (OCR nur überflogen).
- **Alle im 06-12-Report markierten Lückenfüller erledigt:** IV-Rundschreiben-Volltexte, PTBS/Schreckereignis, `BSV_Abklärungsprozess_IV` (→ [[iv-abklaerungsverfahren]]).

## Geprüfte Stichproben (Konsistenz)

- Neueste Seiten (Batches 32–38) alle im [[index]] erfasst und ≥1× eingehend verlinkt: [[weiterentwicklung-iv]], [[kvg-wirtschaftlichkeitspruefung]], [[iv-abklaerungsverfahren]], [[egmr-emrk-svr]], [[plattformarbeit-beitragsstatus]], [[psychische-gesundheit-eingliederung]], [[beweiswert-psychiatrischer-gutachten]], [[neuropsychologische-begutachtung]]. ✅
- WEIV-Reform jetzt über [[weiterentwicklung-iv]] konsolidiert (zuvor verstreut über Art. 44, Tonaufnahmen, Art. 26bis IVV, stufenlose Rente). ✅
- Indikatoren-Achse vollständig: Grundlagen ([[ueberwindbarkeit-grundlagen]]) → Leitentscheid ([[bge-141-v-281]]) → Ausweitung (143 V 409/418, [[bge-145-v-215]]) → Kritik ([[kritik-schmerzrechtsprechung]], [[kritik-indikatorenpraxis-jeger]]). ✅

## Empfohlene nächste Schritte (optional, kein Mangel)

- [[verfahrensfreie-verfuegung]] bei Gelegenheit von `draft` auf `reviewed` ausbauen.
- Inline erwähnte Konzepte mit Ausbaupotenzial (eigene Seite denkbar): *RAD*, *Mahn- und Bedenkzeitverfahren*, *ausserordentliche Bemessungsmethode*, *Wiedererwägung (Art. 53 ATSG)*.
- Künftige Quellen in `raw/Literatur/` lassen sich via `/loop 10m …` erneut automatisiert erschliessen.
