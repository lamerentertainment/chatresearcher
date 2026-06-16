---
title: Lint-Report 2026-06-12
created: 2026-06-12
last_updated: 2026-06-12
source_count: 0
status: reviewed
location: wiki/
---

Gesundheitsprüfung des Wikis nach den Batches 3–15 (Stand: **60 Themenseiten**, 72/191 Literatur-PDFs erschlossen). Geprüft gemäss Lint-Workflow in CLAUDE.md. Methodik: maschinelle Link-/Quellen-/Statusanalyse über alle `wiki/*.md` plus inhaltliche Stichproben. Schweregrade: 🔴 kritisch · 🟡 Warnung · 🔵 Info.

## Zusammenfassung

| Prüfpunkt | Ergebnis |
|-----------|----------|
| Kaputte/ins Leere zeigende Wiki-Links | **0** ✅ |
| Verwaiste Seiten (keine eingehenden Links) | **0** ✅ |
| Seiten ohne jede Quellenangabe | **0** ✅ |
| Widersprüche (markiert) | 6 (alle intentional) |
| Status `draft` | 1 (verfahrensfreie-verfuegung) |
| Status `reviewed` | 58 |

Das Wiki ist strukturell **sehr gesund**: vollständige Verlinkung, durchgängige Quellenangaben, keine Waisen.

## 🔴 Kritisch

Keine.

## 🟡 Warnungen

Keine echten Widersprüche im Sinne sich ausschliessender Behauptungen. Die 6 `WIDERSPRUCH`-Markierungen sind **korrekt** verwendet – sie dokumentieren bewusste Rechts-/Praxisänderungen und nennen jeweils die massgebliche (neuere) Quelle:

1. [[art-43a-atsg]] – Entwurf 2017 vs. geltendes Recht (1.10.2019).
2. [[lse-tabellenlohn]] / [[bge-148-v-174]] – Lehre 2021 vs. Rechtsprechung.
3. [[bger-8c-823-2023]] – Art. 26bis Abs. 3 IVV vs. Bundesgericht.
4. [[depression-invaliditaet]] – frühere Depressionspraxis vs. BGE 143 V 409.
5. [[abhaengigkeitserkrankungen]] – BGer 8C_582/2015 vs. BGE 145 V 215.

→ Kein Handlungsbedarf; bei künftigen Quellen darauf achten, dass die jeweils geltende Rechtslage als massgeblich gekennzeichnet bleibt.

## 🔵 Info / Verbesserungsvorschläge

- **Draft-Seite:** [[verfahrensfreie-verfuegung]] ist bewusst als Kurzeintrag angelegt (OCR-Volltext nur überflogen). Bei Bedarf vertiefen; Backlink aus [[reformatio-in-peius]] ergänzt.
- **Zurückgestellte Grossquelle:** `BSV_Abklärungsprozess_IV.pdf` (316 KB Prozesshandbuch) noch offen – verdient einen eigenen Durchgang (würde [[medizinische-begutachtung]] / IV-Abklärungsverfahren ergänzen).
- **Bekannte Quellenlücken aus früheren Seiten:** [[iv-rundschreiben-339]] vermerkt noch nicht erschlossene Rundschreiben (Nr. 339/334 Volltext, Nr. 298/328/355).
- **Erschliessungsgrad:** 72/191 Literatur-PDFs (≈ 38 %); LGVE-Entscheide weiterhin zuletzt (über opencaselaw), vgl. [[dateistruktur]].

## Konzepte, die erwähnt, aber (noch) nicht als eigene Seite erklärt sind

Keine dangling Wiki-Links. Folgende inline erwähnten Konzepte könnten künftig eigene Seiten erhalten (kein Fehler, nur Ausbaupotenzial): *RAD (Regionaler Ärztlicher Dienst)*, *Mahn- und Bedenkzeitverfahren*, *ausserordentliche Bemessungsmethode*, *Wiedererwägung/prozessuale Revision (Art. 53 ATSG)*.

## Drei vorgeschlagene Artikel zur Lückenfüllung

1. **IV-Rundschreiben Nr. 339/334 (Volltext)** – schliesst die in [[iv-rundschreiben-339]] markierte Lücke zum einheitlichen Gutachtensauftrag.
2. **`BSV_Abklärungsprozess_IV.pdf`** – Hub-Seite zum IV-Abklärungsverfahren (Anknüpfung an [[medizinische-begutachtung]], [[selbsteingliederung-pflicht]]).
3. **Beobachtungs-/Schreckereignis- und PTBS-Rechtsprechung** (vorhandene PDFs: Fleischanderl Schreckereignis SZS 2019; Portmann PTBS) – ergänzt [[depression-invaliditaet]] / [[strukturiertes-beweisverfahren]] um weitere psychische Leiden.

## Geprüfte Stichproben (Konsistenz)

- [[leidensbedingter-abzug]] (max. 25 %) ↔ [[bger-8c-823-2023]] (Pauschalabzug 10 % gesetzwidrig): konsistent als zeitliche Entwicklung dargestellt. ✅
- «55/15-Jahre»-Ausnahme in [[schlussbestimmungen-6a]] ↔ [[rentenrevision]]: konsistent. ✅
- Ausweitung Indikatoren-Rechtsprechung [[bge-141-v-281]] → [[bge-143-v-409]] → [[bge-145-v-215]]: konsistent verkettet. ✅
