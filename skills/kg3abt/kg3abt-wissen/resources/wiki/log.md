# Logbuch

## 2026-06-12 ingest | Neustart der Wissensdatenbank (SVR-Ausrichtung)

Das frühere, strafrechtliche Wiki wurde vom Benutzer geleert (passte nicht zum Schwerpunkt). Neubeginn mit sozialversicherungsrechtlichem Fokus auf Basis des aktuellen `raw/`-Bestands (LGVE 3. Abteilung, Literatur, Statistische Grundlagen, TBS). Gerüst angelegt: [[index]], [[log]], [[dateistruktur]].

Festgelegte Priorität: LGVE-Entscheide zuletzt (grundsätzlich über opencaselaw-MCP erschliessbar). Zuerst Literatur, TBS, Statistische Grundlagen.

## 2026-06-12 ingest | Batch 1 – BGE 141 V 281 (5 Literatur-PDFs)

Erschlossen wurden fünf Beiträge zum Leitentscheid BGE 141 V 281 (Aufgabe der Überwindbarkeitsvermutung). PDFs mit `liteparse` (OCR deu) geparst.

**Quellen (raw/Literatur/):**
1. Mosimann Grundsatzentscheid BGE 141 V 281 HAVE 2015 430.pdf
2. Gächter Meier Einordnung BGE 141 V 281 HAVE 2015 435.pdf
3. Kocher BGE 141 V 281 als Chance für die IV HAVE 2015 S. 442.pdf
4. Fleischanderl Aktuelle Urteile zu BGE 141 V 281 - SZS 2015 557-563.pdf (OCR stark verrauscht – nur als Hinweisgeber auf Folgeurteile genutzt)
5. Riemer_Kafka Zur Ueberwindbarkeit der Ueberwindbarkeitsvermutung szs 2015.pdf

Ergänzend: offizielle Regeste und kanonische Zitation BGE 141 V 281 über den opencaselaw-MCP.

**Erstellte Wiki-Seiten (8):** [[bge-141-v-281]], [[ueberwindbarkeitsvermutung]], [[strukturiertes-beweisverfahren]], [[standardindikatoren]], [[konsistenzpruefung]], [[somatoforme-schmerzstoerung]], [[ausschlussgruende]], [[iv-rundschreiben-339]].

**Offene Punkte:** IV-Rundschreiben Nr. 339 / 334 liegen als PDF vor und sind noch im Volltext zu erschliessen (vgl. [[iv-rundschreiben-339]]).

## 2026-06-12 ingest | Batch 2 – Gemischte Methode / Di Trizio (5 Literatur-PDFs)

Erschlossen wurden fünf Beiträge zur gemischten Methode der Invaliditätsbemessung und ihrer Neuregelung per 1.1.2018 (Folge des EGMR-Urteils Di Trizio). PDFs mit `liteparse` (OCR deu) geparst.

**Quellen (raw/Literatur/):**
1. Änderungen bei der gemischten Methode - Soziale Sicherheit CHSS.pdf
2. Bespr Entsch EMRK gemischte Methode Kieser AJP2016.pdf
3. Hürzeler_Neue gemischte Methode.pdf (Foliensatz; deckt auch UVG und berufliche Vorsorge ab)
4. Renker Jana Neue gemischte Methode.pdf (Jusletter 22.1.2018)
5. IV-Rundschreiben_Nr._372 Gemischte Methode.pdf

Ergänzend: opencaselaw-MCP – Zitationen/Regesten BGE 143 I 50, 144 I 28, 144 I 103, 147 V 124.

**Erstellte Wiki-Seiten (5):** [[invaliditaetsbemessung-methoden]], [[gemischte-methode]], [[egmr-di-trizio]], [[aufgabenbereich-haushalt]], [[iv-rundschreiben-372]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 10 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 3 – Observation / Überwachung (5 Literatur-PDFs)

Erschlossen wurde der Themenblock Observation im Sozialversicherungsrecht (Art. 43a ATSG, EGMR Vukota-Bojić, BGer 9C_806/2016, Beweisverwertung). PDFs neu mit `pdftotext` (Textebene vorhanden, token-sparender als OCR) extrahiert.

**Quellen (raw/Literatur/):**
1. Gächter_Meier_Observation_ein Rechtsinstitut unter Beobachtung.pdf (Jusletter 11.12.2017)
2. Observation Nutzen und Grenzen Aebi Gaechter Aliotta Have 2011.pdf (Personen-Schaden-Forum 2011)
3. Gächter_Meier_Rechtswidrige Observation in der IV_Urteilsbesprechung 9C_806_2016.pdf (Jusletter 14.8.2017)
4. Fleischanderl_Verwertbarkeit_Observation_Rechtsprechung.pdf (SZS 2017 542)
5. Jusletter_observationen-im-soz_50ad496d7c_de.pdf (Weibel, Jusletter 24.2.2020 – Umsetzung)

Ergänzend: opencaselaw-MCP – geltender Wortlaut Art. 43a ATSG, Zitation BGer 9C_806/2016.

**Erstellte Wiki-Seiten (5):** [[observation]], [[art-43a-atsg]], [[egmr-vukota-bojic]], [[bger-9c-806-2016]], [[beweisverwertung-observation]]. Backlinks von [[egmr-di-trizio]] und [[index]].

**Widerspruch markiert:** Entwurf 2017 (E-Art. 43a) vs. geltendes Recht ab 1.10.2019 (Dauer/Mittel), siehe [[art-43a-atsg]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 15 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 4 – Invalideneinkommen / Tabellenlohn (5 Literatur-PDFs)

Erschlossen wurde der Themenblock Invalideneinkommen, LSE-Tabellenlöhne und Korrektive (leidensbedingter Abzug, Parallelisierung) sowie die Reformdebatte 2021 und ihre höchstrichterliche Klärung. PDFs mit `pdftotext` extrahiert (Textebene vorhanden). Mehrere Quellen wurden ausweislich der Dateieigenschaften von der KG 3. Abteilung selbst auf szs.recht.ch bezogen.

**Quellen (raw/Literatur/):**
1. So konkret wie möglich Berechnung des Invaliditätsgrades Meier Egli Filippo Gächter SZS 2021.pdf (SZS 2/2021)
2. Der Weg zu einem invaliditätskonformeren Tabellenlohn_Riemer-Kafka_szs.pdf (SZS 6/2021)
3. Jusletter_invalidenkonforme-ta_73de2ce4cd_de.pdf (Riemer-Kafka et al., Jusletter 22.3.2021)
4. Mosimann_Problemzone Invalideneinkommen.pdf (IRP-HSG-Tagung 5.6.2018)
5. Landolt_Invaliditaetsbemessung bei Schlechtverdienenden.pdf

Ergänzend: opencaselaw-MCP – Regeste BGE 148 V 174, Art. 16 ATSG.

**Erstellte Wiki-Seiten (6):** [[invalideneinkommen]], [[valideneinkommen]], [[lse-tabellenlohn]], [[leidensbedingter-abzug]], [[parallelisierung]], [[bge-148-v-174]]. Backlinks von [[invaliditaetsbemessung-methoden]] und [[index]].

**Widerspruch markiert:** Lehre 2021 (LSE-Medianlöhne überhöht) vs. BGE 148 V 174 (keine Praxisänderung) – in [[lse-tabellenlohn]] und [[bge-148-v-174]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 20 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 5 – IV-Revision 6a / Schlussbestimmungen / Eingliederung aus Rente (5 Literatur-PDFs)

Erschlossen wurde die IV-Revision 6a (in Kraft 1.1.2012): Eingliederungsorientierte Rentenrevision, die umstrittenen Schlussbestimmungen lit. a (Rentenüberprüfung bei unklaren Beschwerdebildern) und ihre höchstrichterliche Absicherung. PDFs mit `pdftotext` extrahiert. Hinweis: `gächter.schlussbestimmungen.6a.pdf` ist inhaltsgleich mit dem Gächter/Kradolfer-Beitrag HAVE 2011 S. 311 (anderer LU-Ausdruck) → effektiv 4 distinkte Quellen.

**Quellen (raw/Literatur/):**
1. Gächter-Kradolfer_Schlussbestimmungen der IVG-Revision 6a, Anwendungsbereich und Problematik_HAVE_2011_S.311.pdf
2. gächter.schlussbestimmungen.6a.pdf (Dublette von 1.)
3. Schär_Übersicht über die Massnahmen der IV-Revision 6a un ihre finanziellen Auswirkungen_HAVE_2011_S.301.pdf
4. Kieser_Eingliederung aus Rente, Entwicklung im Rahmen der 6. IV-Revision_HAVE_2011_S.304.pdf
5. Schär-Jentzsch-Cudré_Die IV-Revision 6a_CHSS 2011_S.244ff..pdf

Ergänzend: opencaselaw-MCP – Regeste BGE 139 V 547.

**Erstellte Wiki-Seiten (4):** [[iv-revision-6a]], [[schlussbestimmungen-6a]], [[eingliederung-aus-rente]], [[bge-139-v-547]]. Backlinks von [[somatoforme-schmerzstoerung]] und [[index]]; Querverbindung zu [[bge-141-v-281]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 25 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 6 – Medizinische Begutachtung / Art. 44 ATSG (4 Literatur-PDFs)

Erschlossen wurde der Begutachtungs-Block: Art. 44 ATSG (rev. 1.1.2022), Beweiswert-Pyramide, polydisziplinäre Vergabe via SuisseMED@P (Zufallsprinzip, BGE 137 V 210), Gerichtsgutachten und Tonaufnahmepflicht (Art. 44 Abs. 6 ATSG). PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Jusletter_art.-44-e-atsg---die_a4079d126f_de.pdf (Girón, 16.9.2019)
2. Jusletter_die-vergabe-der-poly_8a27b69b99_de.pdf (Roger Peter, 16.9.2019)
3. Gerichtsgutachten in der IV SZS 1_2019 S 3 ff.pdf (Furrer, SZS 1/2019)
4. Weiss, Mitwirkungsrechte rund um Tonaufnahmen bei IV-Begutachtungen.pdf (SZS 2023 213)

Ergänzend: opencaselaw-MCP – geltender Wortlaut Art. 44 ATSG.

**Zurückgestellt:** BSV_Abklärungsprozess_IV.pdf (316 KB Volltext, umfangreiches BSV-Prozesshandbuch) – verdient einen eigenen Durchgang, bleibt offen.

**Erstellte Wiki-Seiten (5):** [[medizinische-begutachtung]], [[art-44-atsg]], [[suissemedp-zufallsprinzip]], [[gerichtsgutachten]], [[tonaufnahmen-begutachtung]]. Backlink von [[iv-rundschreiben-339]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 29 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 7 – Verfahrensrecht (5 Literatur-PDFs, 4 distinkt)

Erschlossen wurde ein verfahrensrechtlicher Block: reformatio in peius (Einsprache- vs. Beschwerdeverfahren), aufschiebende Wirkung und unentgeltliche Rechtsverbeiständung. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Reformatio in peius im Einsprache- und Beschwerdeverfahren_SZS.pdf (= Bolt, Kommentar zu BGer 8C_127/2016, SZS 2016 S. 621)
2. Zur reformatio in peius … Kommentar zum Urteil des Bundesgerichtes.pdf (Dublette von 1.)
3. Die drohende Schlechterstellung im Sozialversicherungsprozess_Jaso2012.pdf (Lendfers)
4. Dormann Aufschiebende Wirkung SZS 2019 247.pdf
5. Anspruch auf unentgeltliche.pdf (Weiss, unentgeltliche Rechtsverbeiständung, SZS 2019 S. 39)

Ergänzend: opencaselaw-MCP – Zitation BGer 8C_127/2016.

**Erstellte Wiki-Seiten (3):** [[reformatio-in-peius]], [[aufschiebende-wirkung]], [[unentgeltliche-rechtsverbeistaendung]]. Verlinkt mit [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 34 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 8 – Psychische Leiden: Depression & Sucht (5 Literatur-PDFs)

Erschlossen wurde die Ausweitung der Indikatoren-Rechtsprechung (BGE 141 V 281) auf Depressionen und Abhängigkeitssyndrome. Mehrere PDFs OCR-verrauscht (Umlaute) → sauber paraphrasiert, keine verbatim-Zitate daraus.

**Quellen (raw/Literatur/):**
1. Sager Rechtsprechung Depression SZS 2015 S 308.pdf
2. Slavik Invalidenrentenaspruch bei depressiven Erkrankungen Jusletter.pdf (4.9.2017)
3. HAVE_3-2017_Schleifer_et_al_Depression___Therapieresistenz.pdf
4. Suchtleiden Abhängigkeitserkrankungen Abhandlung_szs16 12ff.pdf (Liebrenz et al., SZS 2016 S. 12)
5. Besprechung BG Urteil 8C_582_2015 Abhängigkeitserkrankung szs 2016 96.pdf

Ergänzend: opencaselaw-MCP – Regesten BGE 143 V 409 und BGE 145 V 215.

**Erstellte Wiki-Seiten (4):** [[depression-invaliditaet]], [[abhaengigkeitserkrankungen]], [[bge-143-v-409]], [[bge-145-v-215]]. Backlinks von [[strukturiertes-beweisverfahren]] und [[index]]; Querverbindung zu [[bge-141-v-281]].

**Widersprüche markiert:** alte Depressions-/Suchtpraxis vs. BGE 143 V 409 / 145 V 215 (je Änderung der Rechtsprechung).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 39 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 9 – Ergänzungsleistungen / EL-Reform (5 Literatur-PDFs)

Neues Themenfeld erschlossen: EL zu AHV/IV, EL-Reform (in Kraft 1.1.2021), Vermögensverzicht und EL als Auffang-Pflegeversicherung. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Eckpunkte der EL-Reform.pdf (Meier/Renker, SZS 1/2020)
2. Dummermuth EL Entwicklung und Tendenzen.pdf (SZS 2/2011)
3. EL_Verzicht.pdf (Früh, Jusletter 20.10.2014)
4. Tuor Vermeidung von Altersarmut mit EL.pdf (SZS 1/2012)
5. Landolt_Die EL als Pflegeversicherung.pdf (SZS 2/2011)

**Erstellte Wiki-Seiten (4):** [[ergaenzungsleistungen]], [[el-reform-2021]], [[vermoegensverzicht-el]], [[el-pflegeversicherung]]. Verlinkt mit [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 44 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 10 – Eingliederung / Selbsteingliederung / Verwertbarkeit im Alter (5 Literatur-PDFs, 4 distinkt)

Erschlossen: Pflicht zur Wiedereingliederung (Art. 8a IVG, BGer 8C_163/2018) und Verwertbarkeit der Restarbeitsfähigkeit bei vorgerücktem Alter. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Eingliederungspflicht BGer Urt 8C_163_2018.pdf (SZS-Rechtsprechung zu 8C_163/2018)
2. Pflicht zur Eingliederung.pdf (Dublette von 1.)
3. Jusletter_pflicht-zur-einglied_c26bdf27cf_de.pdf (Weiss, Urteilsbesprechung)
4. Meier, Eingliederung aus Rente, SZS 2019 125 ff..pdf (SZS 3/2019)
5. Verwertbarkeit Restarbeitsfähigkeit Alter SZS 6_2018 S 630 ff.pdf (Weiss, SZS 6/2018)

Ergänzend: opencaselaw-MCP – Zitation BGer 8C_163/2018.

**Erstellte Wiki-Seiten (3):** [[selbsteingliederung-pflicht]], [[verwertbarkeit-restarbeitsfaehigkeit-alter]], [[bger-8c-163-2018]]. Backlinks von [[eingliederung-aus-rente]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 49 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 11 – Rentenrevision (Art. 17 ATSG) (3 Literatur-PDFs)

Erschlossen: Rentenrevision nach Art. 17 ATSG (Revisionsgrund als bestimmender Faktor, BGer 8C_553/2021), Eingliederung im Revisionsfall bei langjährigen Renten und Begleitmassnahmen nach IV-Revision 6a. PDFs mit `pdftotext` extrahiert; Bucher OCR-verrauscht → paraphrasiert.

**Quellen (raw/Literatur/):**
1. Traub Revisionsgrund szs 2024.pdf (zu BGer 8C_553/2021)
2. Fleischanderl langjährig ausgerichtete Rente Swisslex_SZS 2012 S. 360.pdf
3. Bucher_S_Rentenaufhebung_Herabsetzung_Luzerner_Beiträge.pdf

Ergänzend: opencaselaw-MCP – Zitation BGer 8C_553/2021.

**Erstellte Wiki-Seiten (1):** [[rentenrevision]] (Hub, deckt alle 3 Quellen). Verlinkt mit [[index]], [[eingliederung-aus-rente]], [[bger-8c-163-2018]], [[schlussbestimmungen-6a]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 52 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 12 – Qualitätsleitlinien versicherungspsychiatrische Begutachtung (5 Literatur-PDFs)

Erschlossen: SGPP/SGVP-Qualitätsleitlinien (3. Aufl. 2016) und der SZS-2016-Schwerpunkt zum Dialog Recht/Medizin (Mosimann, Kieser, Bollag, Liebrenz/Schleifer). PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Qualitätsleitlinien für versicherungspsychiatrische Gutachten SGPP SZS 2016 435.pdf
2. Mosimann Hans_Jakob Beitrag der Leitlinien für die Rechtsprechung SZS 2016 507.pdf
3. Kieser Ueli Beitrag der Leitlinien zu Qualitätssicherung und Verteilungsgerechtigkeit … SZS 16 516.pdf
4. Yvonne Bollag Qualitätsleitlinien Beitrag zur Erfüllung des IVG-Zweckes SZS 2016 494.pdf
5. Liebrenz Michael Beitrag der Forschung für die Beurteilung von Leistungsfähigkeit und Prognose SZS 2016 498.pdf

**Erstellte Wiki-Seiten (2):** [[qualitaetsleitlinien-begutachtung]], [[recht-medizin-schnittstelle]]. Backlink von [[medizinische-begutachtung]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 57 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 13 – Observation-Vertiefung & Tabellenlohn-Update (5 Literatur-PDFs, gemischt)

Gemischter Batch: zwei Observations-/Begutachtungsquellen und zwei urteilsbezogene Quellen, die thematisch in andere Cluster gehören. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Schleifer Liebrenz Kieser Verwendung Observationsmaterial psychiatrische Begutachtungen SZS 2019 1.pdf → [[observationsmaterial-begutachtung]]
2. Jusletter_privatdetektive,-auf_cfc41a45f1_de.pdf (Heusser, EGMR-Besprechung) → ergänzt [[egmr-vukota-bojic]]
3. Jusletter_so-nicht--bundesgeri_caf66eb0cd_de.pdf (Meier/Gächter zu BGer 8C_823/2023) → [[bger-8c-823-2023]] (Invalideneinkommen-Cluster!)
4. Jusletter_so-nicht--bundesgeri_caf66eb0cd_de (1).pdf (Dublette von 3.)
5. BGer-Urteil 1C_467_2017 Datenherausgabe.pdf (Transparenz Gutachterstatistik) → ergänzt [[medizinische-begutachtung]]

**Erstellte Wiki-Seiten (2):** [[observationsmaterial-begutachtung]], [[bger-8c-823-2023]]. Backlinks/Ergänzungen in [[observation]], [[egmr-vukota-bojic]], [[leidensbedingter-abzug]], [[lse-tabellenlohn]], [[invalideneinkommen]], [[medizinische-begutachtung]], [[index]].

**Widerspruch markiert:** Art. 26bis Abs. 3 IVV (Pauschalabzug 10 %) vs. BGer 8C_823/2023 (gesetzwidrig).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 62 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 14 – Koordination der Sozialversicherungen (5 Literatur-PDFs)

Neues Themenfeld: BVG-Bindungswirkung von IV-Entscheiden und ALV-Koordination (Taggelder, Vorleistung, Zwischenverdienst). PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Die berufsvorsorgerechtliche Bindungswirkung von IV-Entscheiden … (Moser, AJP 2002 S. 926)
2. Moser_IV-Revisionen_Einflüsse_BVG_Leistungspflicht.pdf
3. Die Koordination von Taggeldern der Arbeitslosenversicherung … (Kieser, ARV 2012 S. 217)
4. Vorleistungspflicht der Arbeitslosenversicherung.pdf (Kaderli/Sakiz, HAVE 2020 S. 368)
5. Das Zwischenverdienstrecht der.pdf (Berner, SZS 2019 S. 17)

**Erstellte Wiki-Seiten (2):** [[bvg-bindungswirkung-iv]], [[alv-koordination]]. Verlinkt mit [[index]], [[iv-revision-6a]], [[eingliederung-aus-rente]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 67 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 15 – Art. 52 AHVG / Rückerstattung / Verfahren (5 Literatur-PDFs)

Erschlossen: Arbeitgeber-/Organhaftung nach Art. 52 AHVG (inkl. Verjährung), Rückerstattung unrechtmässig bezogener Leistungen (Art. 25 ATSG, Gutglaubensschutz) und – als Kurzeintrag – die verfahrensfreie Verfügung. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):**
1. Art. 52 AHVG - Praxis und Zweck der Arbeitgeberhaftung (1).pdf (Groner, SZW 2006)
2. Marc-Hürzeler-Die-Verjährung-von-Forderungen-nach-Art-52-AHVG-HAVE-REAS-2-2025-S-107-ff.pdf
3. Jusletter_die-haftung-der-orga_3da2c802ed_de.pdf (Ballmer, Organhaftung, 1.7.2024)
4. Gutglaubensschutz_Jusletter11775de.pdf (Sennhauser, Art. 25 ATSG)
5. Verfahrensfreie_Verfügung_ZBl 110_2009 S. 593.pdf (Kurzeintrag, draft)

**Erstellte Wiki-Seiten (3):** [[art-52-ahvg-arbeitgeberhaftung]], [[rueckerstattung-gutglaubensschutz]], [[verfahrensfreie-verfuegung]] (draft). Verlinkt mit [[index]], [[ergaenzungsleistungen]], [[alv-koordination]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 72 / 191 PDFs erledigt.

## 2026-06-12 lint | Gesundheitsprüfung nach Batch 3–15

Maschinelle + inhaltliche Prüfung über alle 60 Themenseiten. Ergebnis: **0 kaputte Links, 0 verwaiste Seiten, 0 Seiten ohne Quellenangabe**; 6 WIDERSPRUCH-Marker (alle intentional, dokumentieren Rechtsänderungen); 1 Draft ([[verfahrensfreie-verfuegung]]). Bericht: [[lint-report-2026-06-12]]. Kleinkorrektur: Backlink zu [[verfahrensfreie-verfuegung]] aus [[reformatio-in-peius]] ergänzt. Vorgeschlagene Lückenfüller: IV-Rundschreiben 339/334 Volltext, BSV_Abklärungsprozess_IV.pdf, Schreckereignis/PTBS-Rechtsprechung.

## 2026-06-12 ingest | Batch 16 – UVG: Kausalzusammenhang & Unfallfolgen (5 Literatur-PDFs)

Neues Themenfeld Unfallversicherung: natürlicher/adäquater Kausalzusammenhang, Schreckereignis, Brückensymptome, PTBS und leichte traumatische Hirnverletzung. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):** Jeger (SZS 2025), Fleischanderl Schreckereignis (SZS 2019), Portmann PTBS (zu BGer 8C_483/2012), Brückensymptome (Suva medical 2015), Leichte traumatische Hirnverletzung (Suva medical 2017).

**Erstellte Wiki-Seiten (2):** [[uvg-kausalzusammenhang]], [[unfall-psyche-hirnverletzung]]. Verlinkt mit [[index]], [[strukturiertes-beweisverfahren]], [[ueberwindbarkeitsvermutung]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 77 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 17 – «Neue Schmerzrechtsprechung» / Folgerechtsprechung BGE 141 V 281 (5 Literatur-PDFs)

Vertiefung des BGE-141-V-281-Clusters: Folgerechtsprechung und Lehre (Meier, Kieser ×2, Gächter, Summermatter). In **einer** Hub-Seite gebündelt. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):** Meier «Ein Jahr neue Schmerzrechtsprechung» (Jusletter 2016), Kieser «Wegweiser» + «Blick zurück» (HAVE 2015), Gächter «Schmerzrechtsprechung 2.0», Summermatter Urteilsbesprechung 9C_492/2014.

**Erstellte Wiki-Seiten (1):** [[neue-schmerzrechtsprechung]]. Backlink von [[bge-141-v-281]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 82 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 18 – Beweisrecht & Verfahrensgerechtigkeit (5 Literatur-PDFs)

Erschlossen: Beweisrecht im SV-Prozess (Untersuchungsgrundsatz, Beweisgrad, Beweiswürdigung) und die verfassungs-/verfahrensrechtliche Kritik an der Schmerzrechtsprechung. Hervorzuheben: Rechtsprechungsfundus von M. Wirthlin (Präs. 3. Abt. KG LU). PDFs mit `pdftotext` extrahiert. Eingerichtet im Rahmen des 10-Minuten-/loop (Cron-Job 2a00601d).

**Quellen (raw/Literatur/):** J.P. Müller Verfahrensgerechtigkeit + Gutachten (Kurzfassung), Stolkin Sachverhalt/Recht, Rechtsverwirklichung durch SV-Verfahren (Rez. zu Egli, BGE 137 V 210), Rechtsprechungsfundus Beweisrecht (Wirthlin).

**Erstellte Wiki-Seiten (2):** [[beweisrecht-svprozess]], [[kritik-schmerzrechtsprechung]]. Backlinks von [[neue-schmerzrechtsprechung]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 87 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 19 – UVG: 1. Revision 2017 & Listenverletzungen (5 Quellen / 6 Dateien)

Cron-Iteration (Job 2a00601d). Erschlossen: 1. UVG-Revision 2017, versicherter Verdienst, Beweislast Kausalität sowie unfallähnliche Körperschädigung (Art. 6 Abs. 2 UVG) mit medizinischer Abgrenzung (Rotatorenmanschette, Knie). PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):** Hüsler (Erste UVG-Revision, SZS 2017), Holzer (versicherter Verdienst, SZS 2010), Meier (Beweislast Kausalität, SZS 2017), Lädermann et al. (Rotatorenmanschette), Dubs et al. (Knieschmerzen – 2 Dateifassungen).

Ergänzend: opencaselaw-MCP – Art. 6 UVG (geltend ab 1.1.2017), Regeste BGE 146 V 51.

**Erstellte Wiki-Seiten (2):** [[uvg-leistungen-revision]], [[koerperschaedigung-uvg]]. Verlinkt mit [[index]], [[uvg-kausalzusammenhang]], [[beweisrecht-svprozess]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 93 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 20 – Versicherungspsychiatrische Begutachtung & ICD-11 (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Erschlossen: Methodik der versicherungspsychiatrischen Begutachtung (psychopathologischer Befund/AMDP, Abgrenzung klinische vs. Versicherungspsychiatrie, Medizin/Recht-Schnittstelle) und ICD-10 → ICD-11. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):** Ebner/Herzog-Zwitter (psychopathologischer Befund, SZS 2024), Kurmann (Einführung Psychopathologie), RAD (Evidenzbasierte Versicherungspsychiatrie), Liebrenz et al. (Medizin/Recht, 2013), Stieglitz/Ebner (ICD-11).

**Erstellte Wiki-Seiten (2):** [[versicherungspsychiatrische-begutachtung]], [[icd-11]]. Backlink von [[medizinische-begutachtung]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 98 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 21 – IV-Revision 6a-Vertiefung & Rechtsprechungsübersichten (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Vertiefung Schlussbestimmungen 6a (Gächter/Siki «Sparen um jeden Preis?», Fleischanderl 6a-Urteile), kritische Urteilsbesprechung zur Ressourcen-Anwendung (Egli/Slavik zu BGer 8C_703/2018) und eine Referenzseite für die periodischen Rechtsprechungsübersichten. PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):** Gächter/Siki (IVG 6a), Fleischanderl 6a-Urteile (SZS 2014), Egli/Slavik (8C_703/2018), Gächter/Meier Rechtsprechungsübersichten SZS 2016 + 2017.

**Erstellte Wiki-Seiten (1):** [[rechtsprechungsuebersichten-svr]]. **Angereichert:** [[schlussbestimmungen-6a]] (Gächter/Siki + Folgerechtsprechung), [[standardindikatoren]] (Kritik Egli/Slavik an der Ressourcen-Anwendung; Backlink zu [[depression-invaliditaet]]).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 103 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 22 – Hilflosenentschädigung, UV-Pflege & Güterichter (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Zwei Mini-Cluster: (1) Hilflosenentschädigung/Pflege (HE + Intensivpflegezuschlag Minderjährige, Kinder mit Diabetes Typ 1, UV-Pflegeleistungen Tetraplegie); (2) Güterichter/Mediation (deutsches Sozialprozessrecht, komparativ). PDFs mit `pdftotext` extrahiert. Hinweis: «Leitfaden HLSG 2014» = Hessisches LSG (Güterichter), nicht Hilflosigkeit.

**Quellen (raw/Literatur/):** Sarbach/Süsstrunk (HE/Intensivpflegezuschlag), Brugger Schmidt/Tremp (Kinder Diabetes HE, SZS 2020), Urteilsbesprechung 8C_626/2024 (UV-Pflege Tetraplegie), Brändle/Schreiber (Güterichter, WzS 2014), Leitfaden HLSG 2014.

**Erstellte Wiki-Seiten (3):** [[hilflosenentschaedigung]], [[uv-pflegeleistungen]], [[gueterichter-mediation]]. Verlinkt mit [[index]], [[el-pflegeversicherung]], [[beweisrecht-svprozess]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 108 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 23 – Jeger: invaliditätsfremde Faktoren & Kritik an der Indikatorenpraxis (6 Dateien)

Cron-Iteration (Job 2a00601d). Jeger-Cluster: invaliditätsfremde Faktoren in Gutachten, «garbage in – garbage out» (Fragestellung), sowie die medizinische Kritik am «Rückfall» des BG nach BGE 141 V 281. PDFs mit `pdftotext` extrahiert. Hinweis: «Jeger Hirnkappe.pdf» ist interne Korrespondenz (kurz), nur als Quelle vermerkt.

**Quellen (raw/Literatur/):** Jeger invaliditätsfremde Faktoren (SZS 2023, 2 Fassungen), Jeger «garbage in – garbage out», Jeger zu BGE 148 V 49 (+ 144 V 50, 145 V 361), Jeger neue Schmerzrechtsprechung (2015), Jeger Hirnkappe.

**Erstellte Wiki-Seiten (2):** [[invaliditaetsfremde-faktoren]], [[kritik-indikatorenpraxis-jeger]]. Backlink von [[depression-invaliditaet]] und [[index]]; Querverbindung zu [[kritik-schmerzrechtsprechung]], [[standardindikatoren]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 114 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 24 – Begutachtungsverfahren-Praxis (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Vertiefung des Begutachtungs-Clusters: neues Verfahren (Art. 72bis IVV / BGE 137 V 210), SuisseMED@P-Reporting, neuropsychologische Begutachtung, «Richter als Gutachter». PDFs mit `pdftotext` extrahiert.

**Quellen (raw/Literatur/):** Glättli (neues Begutachtungsverfahren, Art. 72bis IVV), Canela et al. 2015 (IV-Begutachtung Überblick), SuisseMED@P Reporting 2013 (BSV), Weiss (neuropsychologischer Gutachter), Manuela Mosimann (Richter als Gutachter, Art. 183 ZPO).

**Erstellte Wiki-Seiten (1):** [[neuropsychologische-begutachtung]]. **Angereichert:** [[suissemedp-zufallsprinzip]] (Art. 72bis IVV + Reporting), [[gerichtsgutachten]] (Abgrenzung «Richter als Gutachter»).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 119 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 25 – Medizinische Grundlagen der Überwindbarkeit/Indikatoren (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Foundational-Block: die medizinisch-wissenschaftlichen Vorläufer der Indikatorenrechtsprechung (Henningsen, Mosimann «Perspektiven der Überwindbarkeit», Dohrenbusch zur «zumutbaren Willensanspannung»). PDFs mit `pdftotext` extrahiert. Hinweis: «Müller.somatoformeSchmerzstörung» = Vollfassung des bereits in Batch 18 erfassten J.P.-Müller-Gutachtens → [[kritik-schmerzrechtsprechung]] ergänzt.

**Quellen (raw/Literatur/):** Henningsen (SZS 2014 + Gutachten TU München), Mosimann (Überwindbarkeit SZS 2014), Dohrenbusch (zumutbare Willensanspannung 2013), Müller (somatoforme Schmerzstörung, Vollfassung).

**Erstellte Wiki-Seiten (1):** [[ueberwindbarkeit-grundlagen]]. Backlinks von [[ueberwindbarkeitsvermutung]], [[standardindikatoren]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 124 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 26 – Verfahrensrecht-Besonderheiten & kantonale Praxis LU (5 Quellen / 7 Dateien)

Cron-Iteration (Job 2a00601d). Verfahrenspraxis: Zustellung ins Ausland (Volz), E-Dossier/Digitalisierung (Tschümperlin), kantonale Verfahren Luzern (Burch/Kriesi) + VRG-Revision 2015; dazu die Gächter-Verfahrensrechts-Übersicht ZBJV 153/2017. PDFs mit `pdftotext`. Zwei Dublettenpaare erkannt (Gächter Verfahrensrecht ZBJV; Volz Zustellung).

**Erstellte Wiki-Seiten (1):** [[sv-verfahren-besonderheiten]]. **Angereichert:** [[rechtsprechungsuebersichten-svr]] (Gächter Verfahrensrecht 2013–2015).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 131 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 27 – Beweiswert & Qualität psychiatrischer Gutachten (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Beweiswert/Qualität psychiatrischer Gutachten (Bollinger, Meyer, Liebrenz, Haab/Mösch Payot Prüfsystem) + BSV-Liste der IV-Gutachten 2021. PDFs mit `pdftotext`. Massstab BGE 125 V 351.

**Erstellte Wiki-Seiten (1):** [[beweiswert-psychiatrischer-gutachten]]. Backlink von [[versicherungspsychiatrische-begutachtung]] und [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 136 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 28 – Invaliditätsbemessung-Vertiefung (5 Quellen / 6 Dateien)

Cron-Iteration (Job 2a00601d). Reine Vertiefung bestehender Seiten (keine neue Seite). Grundprobleme-Rechtsgutachten (Gächter/Coop), Ableitung Invalideneinkommen aus LSE (Ionta), Quartalsschätzungen/Lohnentwicklung (Berner SZS 2025), Statusbestimmung & Gleichbehandlung Frau/Mann (Brändli), Methodenüberblick (Mosimann 2008). PDFs mit `pdftotext`. Grundprobleme in 2 Dateifassungen.

**Angereichert:** [[invalideneinkommen]] (Grundprobleme-Rechtsgutachten + Festlegung/Anpassung der Vergleichseinkommen: Ionta, Berner), [[invaliditaetsbemessung-methoden]] (Statusbestimmung/Gleichbehandlung Brändli + Mosimann-Überblick).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 142 / 191 PDFs erledigt.

## 2026-06-12 ingest | Batch 29 – IV-Rundschreiben des BSV (6 Dateien) – schliesst Lint-Lücke

Cron-Iteration (Job 2a00601d). Erschlossen: IV-Rundschreiben Nr. 298 (GG 404), 328 (LSE 2012), 334 (Beweisverfahren psychosomatische Leiden, zu 9C_492/2014), 339 (Gutachtensauftrag + Anhang), 355 (gemischte Methode / Di Trizio). Damit ist die im [[lint-report-2026-06-12]] markierte Rundschreiben-Lücke geschlossen. PDFs mit `pdftotext`.

**Erstellte Wiki-Seiten (1):** [[iv-rundschreiben-uebersicht]] (Hub Nr. 298/328/334/339/355/372). **Angereichert:** [[iv-rundschreiben-339]] (Volltext erschlossen, «noch nicht erschlossen»-Vermerk entfernt).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 148 / 191 PDFs erledigt.

## 2026-06-13 ingest | Batch 30 – Indikatoren-/Konsistenz-Vertiefung (6 Dateien)

Cron-Iteration (Job 2a00601d). Reine Vertiefung (keine neue Seite): Ausweitung der Indikatorenrechtsprechung auf alle psychischen Leiden (BGE 143 V 418), Konsistenzindikatoren-Bilanz, Jeger-Vortrag, SAPPM/SGSS-Schmerzleitlinien, ALV-Arbeits-/Erwerbsunfähigkeit. PDFs mit `pdftotext`.

**Angereichert:** [[konsistenzpruefung]] (Meier, BGE 143 V 418), [[bge-143-v-409]] (BGE 143 V 418 / Gächter-Folien), [[qualitaetsleitlinien-begutachtung]] (SAPPM/SGSS-Schmerzleitlinien), [[kritik-indikatorenpraxis-jeger]] (Jeger-Vortrag), [[alv-koordination]] (Merz ARV 2018).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 154 / 191 PDFs erledigt.

## 2026-06-13 ingest | Batch 31 – Psychische Gesundheit, Arbeitsplatz & Eingliederung (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Sozial-/forschungspolitische Aspekte psychischer Gesundheit & Beschäftigung, junge psychisch Kranke (FoP2-IV), arbeitsplatzbezogene Arbeitsunfähigkeit (BGer 1C_595/2023), Neuroimaging (NZZ). PDFs mit `pdftotext`. EL-Reform-Quelle (Schüpbach) korrekt zur EL-Seite umgeleitet.

**Erstellte Wiki-Seiten (1):** [[psychische-gesundheit-eingliederung]]. **Angereichert:** [[el-reform-2021]] (Schüpbach CHSS 2019).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 159 / 191 PDFs erledigt.

## 2026-06-13 lint | Zweite Gesundheitsprüfung (nach Batches 18–31)

Auf Wunsch des Benutzers statt eines Ingest-Batches durchgeführt (der angefangene EGMR/EMRK-Batch wurde verworfen – keine Wiki-Änderungen, nur Extraktion). Ergebnis über 78 Themenseiten: **0 kaputte Links, 0 Waisen, 0 Quellenlücken, 0 schwache Knoten**; 6 WIDERSPRUCH-Seiten (intentional); 1 Draft. Ein False Positive (wörtlicher Wiki-Link-Beispieltext) im [[lint-report-2026-06-12]] neutralisiert. Erledigte Lückenfüller seit letztem Lint: IV-Rundschreiben-Volltexte, PTBS/Schreckereignis, BGE 143 V 418. Bericht: [[lint-report-2026-06-13]]. Nächster sinnvoller Ingest: EGMR/EMRK-Cluster (Kradolfer, Dumermuth, M. Müller, Pärli).

## 2026-06-13 ingest | Batch 32 – EGMR/EMRK, Plattformarbeit & Verwaltungsrechtsschutz (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). EGMR/EMRK im SVR (Kradolfer Leistungsabbau, Dumermuth Standortbestimmung), Plattformarbeit/Beitragsstatus (Pärli Uber), Verwaltungsrechtsschutz (M. Müller). PDFs mit `pdftotext`. «Aspekte rechtlicher Nähebeziehungen» (FS Aebi-Müller) nur Randbezug → vermerkt, nicht separat erschlossen.

**Erstellte Wiki-Seiten (2):** [[egmr-emrk-svr]], [[plattformarbeit-beitragsstatus]]. **Angereichert:** [[sv-verfahren-besonderheiten]] (M. Müller). Backlinks von [[egmr-vukota-bojic]], [[egmr-di-trizio]], [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 164 / 191 PDFs erledigt.

## 2026-06-13 ingest | Batch 33 – Rechtsprechungsübersichten & Foundational (5 Literatur-PDFs)

Cron-Iteration (Job 2a00601d). Reine Vertiefung (keine neue Seite): Hürzeler/Biaggi-Übersicht 2015/2016 (ZBJV 153/2017, I–III + IV), Gächter Verfahrensrecht 2012 (ZBJV 149/2013), BGE-137-V-210-Zusammenfassung, Liebrenz et al. forensisch-psychiatrische Begutachtung (AJP 2018). PDFs mit `pdftotext`.

**Angereichert:** [[rechtsprechungsuebersichten-svr]] (Tabelle um Hürzeler/Biaggi + Gächter-Verfahrensrecht 2012/2013–2015 erweitert), [[suissemedp-zufallsprinzip]] (137-V-210-Zusammenfassung), [[beweiswert-psychiatrischer-gutachten]] (Liebrenz AJP 2018).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 169 / 191 PDFs erledigt.

## 2026-06-13 ingest | Batch 34 – Begutachtungs-Reste & ICD-11 (5 Dateien)

Cron-Iteration (Job 2a00601d). Reine Vertiefung: Traub zum Beizug vorbefasster Sachverständiger (Ausstand), IBP/Thoma ICD-11-Handouts, Samuelsson zu BGer 8C_972/2012 (Überwindbarkeitspraxis vor 141 V 281). PDFs mit `pdftotext`. «2019_Rechtliche und praktische Aspekte Gerichtsgutachten» = Dublette des Furrer-Beitrags (bereits in [[gerichtsgutachten]]).

**Angereichert:** [[medizinische-begutachtung]] (Traub, Ausstand vorbefasster Gutachter), [[icd-11]] (IBP/Thoma-Handouts), [[ueberwindbarkeit-grundlagen]] (Samuelsson, 8C_972/2012).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 174 / 191 PDFs erledigt.

## 2026-06-13 ingest | Batch 35 – WEIV-Reform & öffentliche Debatte (5 Dateien)

Cron-Iteration (Job 2a00601d). «Weiterentwicklung der IV» (WEIV) als Reform-Hub: Hablützel «Pflästerlipolitik», Haag «Durchzogene Bilanz» (MEDAS), NZZ-Medienbeiträge (vermessene Psychiatrie / Missbrauch). PDFs mit `pdftotext`. «LANG JaSo 2022» Thema aus TOC nicht eindeutig → vermerkt, nicht separat erschlossen.

**Erstellte Wiki-Seiten (1):** [[weiterentwicklung-iv]] (bündelt Art. 44 ATSG, Tonaufnahmen, stufenlose Rente Art. 28b, Art. 26bis IVV / 8C_823/2023). **Angereichert:** [[kritik-schmerzrechtsprechung]] (mediale Debatte NZZ). Backlinks von [[art-44-atsg]], [[index]].

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 179 / 191 PDFs erledigt.

## 2026-06-13 ingest | Batch 36 – KV/UV/Verfahren-Reste (5 Dateien)

Cron-Iteration (Job 2a00601d). Eugster KVG-Wirtschaftlichkeitsprüfung (neue Seite), Ackermann SV-Prozess Bern + Grundriss (Verfahren-Referenz), Landolt UV-Pflegeentschädigung, Caderas/Hürzeler Observation (Vukota-Bojić). PDFs mit `pdftotext`.

**Erstellte Wiki-Seiten (1):** [[kvg-wirtschaftlichkeitspruefung]]. **Angereichert:** [[sv-verfahren-besonderheiten]] (Ackermann/Bern, Grundriss), [[uv-pflegeleistungen]] (Landolt), [[egmr-vukota-bojic]] (Caderas/Hürzeler).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 184 / 191 PDFs erledigt.

## 2026-06-13 ingest | Batch 37 – IV-Abklärungsprozess & Verwaltungsdokumente (5 Dateien)

Cron-Iteration (Job 2a00601d). Die zurückgestellte Grossquelle `BSV_Abklärungsprozess_IV.pdf` (Forschungsbericht 4/15, FoP2-IV) erschlossen; SECO-ALV-Audit als Quelle vermerkt; BAG-/SÄZ-/EKAS-Dokumente als Randdokumente ehrlich vermerkt (nicht separat erschlossen). PDFs mit `pdftotext`.

**Erstellte Wiki-Seiten (1):** [[iv-abklaerungsverfahren]] (prozessualer Hintergrund zu Begutachtung/Eingliederung/Einkommensvergleich). **Angereichert:** [[alv-koordination]] (SECO-Audit).

**Ingest-Status:** [[literatur-ingest-status]] aktualisiert → 189 / 191 PDFs erledigt. Es verbleiben 2 Randstücke (Gächter Erbrecht, Leistungsvereinbarung BSV) ohne SVR-Schwerpunktbezug.

## 2026-06-13 ingest | Batch 38 (Abschluss) – letzte 2 Randstücke → Bestand vollständig

Cron-Iteration (Job 2a00601d). Nur noch 2 offene Dateien (keine 5): Gächter «Wozu noch Erbrecht?» (Pflegefinanzierung/Erbrecht → [[el-pflegeversicherung]] verknüpft) und Leistungsvereinbarung BSV 2012 (Verwaltungsdokument, off-core, nicht separat erschlossen).

**Damit sind alle 191/191 Literatur-PDFs abgehakt.** Der thematisch relevante Bestand ist vollständig ins Wiki überführt (83 Themenseiten); die nicht separat erschlossenen Einträge sind Dubletten oder Verwaltungs-/Randdokumente, jeweils im Status vermerkt.

**Empfehlung:** Cron-Loop beenden (`CronDelete 2a00601d`); optional abschliessender Lint-Durchgang.

## 2026-06-13 lint | Abschluss-Gesundheitsprüfung (nach vollständigem Ingest)

Ingest-Loop gestoppt (Cron `2a00601d` gelöscht; CronList leer). Prüfung über 83 Themenseiten: **0 kaputte Links, 0 Waisen, 0 Quellenlücken, 0 schwache Knoten**; 6 WIDERSPRUCH-Seiten (intentional); 1 Draft. Alle Seiten der Batches 32–38 im Index erfasst und verlinkt. Bericht: [[lint-report-2026-06-13-abschluss]]. **Literatur-Ingest abgeschlossen: 191/191 PDFs, 83 Themenseiten.**

## 2026-06-13 ingest | Statistische Grundlagen (Inventar, keine inhaltliche Erfassung)

Auf Wunsch des Benutzers **nur ein Inventar** von `raw/Statistische Grundlagen/` erstellt (was ist vorhanden, wo zu finden) – ausdrücklich keine inhaltliche/Werte-Erschliessung. Verzeichnislisting via `find`. Bestand: LSE-Vollpublikationen (PDF 2004–2012), LSE-Excel-Tabellen (TA1/T1/T1b/T17/T18/TA12/T7, Jahrgänge 2014–2024), Nominallohnindizes (Basis 1993/2010/2015/2020), betriebsübliche Arbeitszeit (NOGA 2008), IV-Rundschreiben Nr. 328.

**Erstellte Wiki-Seiten (1):** [[statistische-grundlagen]] (Inventar mit Pfaden). **Angereichert/verlinkt:** [[dateistruktur]], [[lse-tabellenlohn]], [[invalideneinkommen]], [[index]].

## 2026-06-13 ingest | Textbausteine (TBS) – Finder mit Codierung & Artikel-Index

`raw/TBS/` erschlossen (5 DOCX via `textutil` extrahiert, Struktur analysiert). Erstellt als **Finder**, nicht als Volltext-Dump: Codierungssystem (ATxx/IVxx/UVxx, Verordnung …Vxx, Absätze/Versionen), 5 Sammlungen mit Gültigkeit (ATSG/IVG je 21er bis 31.12.2021 + 22er ab 1.1.2022; UVG aktuell), und Index der abgedeckten Artikel je Sammlung. Bausteintexte bleiben in den DOCX. Differenz 21→22: ATSG neu Art. 17; IVV neu Art. 25/26 (u. a. 26bis).

**Erstellte Wiki-Seiten (1):** [[textbausteine]]. **Angereichert/verlinkt:** [[dateistruktur]], [[index]] + Querverweise zu den einschlägigen Themenseiten (Art. 16/17/44 ATSG, Art. 8a/28a IVG, Art. 6 UVG …).

## 2026-06-13 ingest | LGVE 3. Abteilung – Index & Methode gesichert (Inhalt steht aus)

`raw/LGVE 3. Abteilung/` erkundet: **846 Entscheide (1981–2025)**, nach Jahr abgelegt, Zitierform `LGVE [Jahr] III Nr. [N]`. **Befund:** die PDFs sind gescannte Bilder **ohne Textebene** (`pdftotext` leer) → Inhalt nur per OCR oder über opencaselaw. **opencaselaw war zum Zeitpunkt nicht erreichbar** (Fehler −32602), daher konnte der inhaltliche Ingest (Regeste + opencaselaw-Link je Entscheid) noch nicht erfolgen.

**Jetzt gesichert (durable, da `raw/` künftig nicht mehr zugänglich):** vollständiger **Index** aller 846 Entscheide pro Jahr inkl. Lücken (2012 ohne Nr. 4/12), Doppeleintrag (2024 Nr. 4) und 2 «Internetentscheide» (2023: Aktenzeichen **5V 21 350**). Plus dokumentierte **Erschliessungsmethode/Workflow** für den opencaselaw-Abruf.

**Erstellte Wiki-Seiten (1):** [[lgve-3-abteilung]] (`status: needs_update` bis Inhalt erschlossen). **Verlinkt:** [[dateistruktur]], [[index]].

**Nächster Schritt:** sobald opencaselaw verfügbar – inhaltlicher Ingest jahrgangsweise (2020–2025 zuerst), als `/loop`-Aufgabe.

## [2026-06-13] ingest | LGVE-Jahrgang 2025 inhaltlich erschlossen (opencaselaw lu_gerichte)

opencaselaw-MCP (Sammlung `lu_gerichte`) ist wieder erreichbar – inhaltlicher Ingest gestartet, jahrgangsweise rückwärts ab 2025 (`/loop`-Aufgabe, alle 10 Min., Job 1422c663).

**Erschlossen: LGVE 2025 III** – 6 nummerierte Leitentscheide + 1 Internetentscheid, je mit amtlicher Regeste, Aktenzeichen, Datum und opencaselaw-Link:
- Nr. 1 = 5V 23 272 (IV, externe Begutachtung zu Hause; ME/CFS; Art. 43 ATSG)
- Nr. 2 = 5V 23 150 (AHV, asymmetrische Dividenden als beitragspflichtiger Lohn; Art. 5 Abs. 2 AHVG)
- Nr. 3 = 5V 23 135 (EL, Einkommensverzicht zugunsten Verwandtenunterstützung = rechtsmissbräuchlich; Art. 11 Abs. 3 lit. a ELG)
- Nr. 4 = 5V 24 280 (IV, Pauschalabzug Art. 26bis Abs. 3 IVV / Revisionsgrund Übergangsbestimmung)
- Nr. 5 = SG 24 1 (KVG-Schiedsgericht, paritätische Vertrauenskommission; Art. 89 KVG)
- Nr. 6 = 5V 24 328 (IV/WEIV, keine abschliessende Entscheidkompetenz der IV-Stelle über externes Gutachten; Art. 44 ATSG, Art. 6 EMRK) – Datum 18.07.2025 (opencaselaw-Metadatum «01.01.2022» fehlerhaft)
- Internetentscheid = 5V 23 211/5V 24 48 (ALV, Beweismass Einstellungsgrund; vernichtete Unterlagen)

**Neue Seite (1):** [[lgve-2025-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Abschnitt «Inhaltlich erschlossene Jahrgänge», Status-Hinweis), [[index]] (87 Seiten). **Backlinks ergänzt:** [[art-44-atsg]], [[weiterentwicklung-iv]], [[invalideneinkommen]], [[vermoegensverzicht-el]], [[alv-koordination]].

**Nächster Schritt:** Jahrgang 2024 (12 Entscheide, Nr. 1–11 + Doppeleintrag) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2024 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2024 III Nr. 1–11** (kein Internetentscheid), je mit amtlicher Regeste, Aktenzeichen, Datum und opencaselaw-Link:
- Nr. 1 = 5V 22 402 (KVG, SRS Ausland/Thailand, keine OKP-Leistungspflicht)
- Nr. 2 = 5V 23 203 (IV, monodisziplinäres Gutachten: Einigungsversuch zwingend)
- Nr. 3 = 5V 23 171 (EL, Kalenderjahrpraxis; Nutzniessungsverzicht jährlich anrechenbar)
- Nr. 4 = 5V 22 26 (IV, ME/CFS = Krankheit; Prüfung nach Standardindikatoren)
- Nr. 5 = 5V 23 229 (IV/WEIV, keine endgültige Entscheidkompetenz über Gutachtensart; Erstbegutachtung grds. polydisziplinär) – Datum 27.02.2024 (opencaselaw-Metadatum «01.01.2022» fehlerhaft)
- Nr. 6 = 5V 22 194 (IV-Rückforderung: Verwirkungsfrist uno actu; Rechtsnatur Rückforderungsverfügung)
- Nr. 7 = 5V 22 179 (IV, Rückerstattung Kinderrenten; Gegenstandslosigkeit)
- Nr. 8 = 5V 22 180 (IV, Rückforderung an Dritte: kein Vorbescheidverfahren)
- Nr. 9 = 5V 24 102 (KVG, WEKO-Legitimation; BGBM nicht anwendbar bei OKP-Zulassung, lex specialis)
- Nr. 10 = 5V 20 18 (IV, separate Rückforderungsverfügung = eigenständig anfechtbar)
- Nr. 11 = 5V 21 352 (AHV, asymmetrische Dividenden; 10-%-Grenze + branchenüblicher Lohn)

Aktenzeichen für Nr. 1/4/11 (in opencaselaw-FTS schwer auffindbar) aus den Entscheidköpfen der raw-PDFs verifiziert.

**Neue Seite (1):** [[lgve-2024-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2023), [[index]] (88 Seiten). **Backlinks ergänzt:** [[rueckerstattung-gutglaubensschutz]] (Cluster Nr. 6/7/8/10), [[standardindikatoren]] (Nr. 4 ME/CFS), [[art-44-atsg]] (Nr. 2/5). **Querverlinkt:** [[lgve-2025-iii]] (ME/CFS 2024 Nr. 4 ↔ 2025 Nr. 1; Dividenden 2024 Nr. 11 ↔ 2025 Nr. 2).

**Nächster Schritt:** Jahrgang 2023 (Nr. 1–7 + Internetentscheid 5V 21 350) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2023 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2023 III Nr. 1–7 + Internetentscheid**, je mit amtlicher Regeste, Aktenzeichen, Datum und opencaselaw-Link:
- Nr. 1 = 5Q 21 10 (Berufl. Vorsorge, Säule 3a fällt nicht in Nachlass; Willensvollstrecker nicht aktivlegitimiert)
- Nr. 2 = 5V 21 387 (UVG/KVG, Kanton nach Art. 49a KVG kein Versicherungsträger; kein Anspruch auf Verfügung)
- Nr. 3 = 5V 22 71 (IV, Assistenzbeitrag: Konkubinatspartner der Mutter ≠ Assistenzperson)
- Nr. 4 = 5V 22 368 (EO, Zivildienst: Erlöschen nach 5 Jahren; Begriff «Dienst»)
- Nr. 5 = 5V 21 454 (UVG, Überentschädigung: Anwaltskosten als anrechenbare Mehrkosten)
- Nr. 6 = 5V 22 239 (IV, Spitex-Abrechnungsberechtigung ohne Tarifvertragsbeitritt)
- Nr. 7 = 5V 23 70 (AHV, Witwerrente/EGMR Beeler 78630/12: keine Revision/Wiedererwägung) – LU-Datum 28.08.2023 (opencaselaw-Metadatum übernahm fälschlich das EGMR-Urteilsdatum 11.10.2022)
- Internetentscheid = 5V 21 350 (Militärversicherung, Morbus Bechterew/Uveitis: 50-%-Haftungsbeschränkung, res iudicata)

Aktenzeichen/Daten aus den Entscheidköpfen der raw-PDFs verifiziert.

**Neue Seite (1):** [[lgve-2023-iii]] (`status: reviewed`), inkl. Abschnitt «Noch nicht erschlossene Konzepte» (Kandidaten für eigene Seiten: Säule 3a/BVG, EO/EOG, Assistenzbeitrag, Witwen-/Witwerrente & EGMR Beeler, Militärversicherung). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2022), [[index]] (89 Seiten). **Backlinks ergänzt:** [[egmr-emrk-svr]] (Nr. 7 Beeler), [[hilflosenentschaedigung]] (Nr. 3 Assistenzbeitrag), [[uvg-leistungen-revision]] (Nr. 5 Überentschädigung).

**Nächster Schritt:** Jahrgang 2022 (Nr. 1–3) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2022 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2022 III Nr. 1–3** (kein Internetentscheid):
- Nr. 1 = 5V 21 401 (EO, auch bei Mehrlingsgeburt nur eine Vaterschaftsentschädigung) – LU-Datum 14.04.2022 (opencaselaw-Metadatum 09.09.2021 = Verfügungsdatum)
- Nr. 2 = 5V 21 320 (IV/AHV, Kinderrente: Sprachaufenthalt als Teil der durchgehenden Ausbildung; Art. 49ter Abs. 3 lit. a AHVV)
- Nr. 3 = 5V 22 47 (ALV, Befreiung von der Beitragszeit wegen Krankheit; Taggelder > 12 Monate)

**Neue Seite (1):** [[lgve-2022-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2021), [[index]] (90 Seiten). **Backlink ergänzt:** [[alv-koordination]] (Nr. 3). Offene Konzept-Kandidaten (EO/EOG, Kinderrente/Ausbildungsbegriff) auf der Jahresseite vermerkt.

**Nächster Schritt:** Jahrgang 2021 (Nr. 1–5) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2021 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2021 III Nr. 1–5** (kein Internetentscheid):
- Nr. 1 = 5V 20 77 (AHV, unentgeltliches Wohnrecht ≠ selbständiges Erwerbseinkommen) – LU-Datum 28.10.2020 (Metadatum 04.10.2019 = Verfügung)
- Nr. 2 = 5V 20 396 (ALV, Corona-Kurzarbeit: Ferien-/Feiertagsentschädigung bei Monatslöhnern; Covid-19-V/SECO-Weisung ohne Grundlage; BGer 8C_272/2021)
- Nr. 3 = 5V 21 99 (ALV, Rückforderung nach Art. 29 AVIG: ungerechtfertigte Bereicherung; Verrechnung nur bis Existenzminimum)
- Nr. 4 = 5V 21 93 (AHV, Familienzulage mit Sozialleistungscharakter vom massgebenden Lohn ausgenommen; WML Rz. 2170/2171 unangewendet)
- Nr. 5 = 5V 19 339 (KVG, Pflege-Restkostenfinanzierung: Zuständigkeit KG nach § 17 BPG; ATSG-Verfahren nicht zugeschnitten)

**Neue Seite (1):** [[lgve-2021-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2020), [[index]] (91 Seiten). **Backlinks ergänzt:** [[plattformarbeit-beitragsstatus]] (neuer Abschnitt AHV-Beitragsrecht/massgebender Lohn als Hub: 2021 Nr. 1/4 + 2024 Nr. 11 + 2025 Nr. 2), [[alv-koordination]] (Nr. 2/3), [[rueckerstattung-gutglaubensschutz]] (Nr. 3).

**Beobachtung:** Wiederkehrendes Muster in der LU-Beitragsrechtsprechung – Verwaltungsweisungen (WML, KSVI, SECO/Covid-19-V) wird bei Widerspruch zu Gesetz/Verordnung die Anwendung versagt (2021 Nr. 2 und Nr. 4; vgl. 2024 III Nr. 5, 2025 III Nr. 6).

**Nächster Schritt:** Jahrgang 2020 (Nr. 1–5) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2020 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2020 III Nr. 1–5** (kein Internetentscheid):
- Nr. 1 = 5V 18 268 (AHV-Schadenersatz, Art. 52 AHVG: keine Organhaftung für vor Organstellung – mit Verlustschein – eingetretenen Schaden)
- Nr. 2 = 5V 19 52 (AHV, Fahrschulkosten für Lernende = massgebender Lohn)
- Nr. 3 = 5V 18 294/5V 19 27 (ALV, kein Raum für Art. 40b AVIV bei vorbestehender Gesundheitseinschränkung)
- Nr. 4 = 5V 18 163 (EL, zu tiefe kantonale Pflegeheim-Tagestaxe verstösst gegen Bundesrecht; konkrete Normenkontrolle, Norm unangewendet)
- Nr. 5 = 5V 19 40 (AHV, Kapitalgewinn Geschäfts- → Privatvermögen; FLG-Familienzulagenbeiträge; Verzugszins Art. 41bis AHVV)

Alle Daten stimmten diesmal mit den opencaselaw-Metadaten überein (ältere Jahrgänge zuverlässiger).

**Neue Seite (1):** [[lgve-2020-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2019), [[index]] (92 Seiten). **Backlinks ergänzt:** [[art-52-ahvg-arbeitgeberhaftung]] (Nr. 1 – direkter Konzept-Treffer), [[el-pflegeversicherung]] (Nr. 4), [[plattformarbeit-beitragsstatus]] (Nr. 2/5 im AHV-Beitrags-Hub).

**Beobachtung:** Das Muster «kantonale/Verwaltungsnorm bei Bundesrechtswidrigkeit unangewendet» setzt sich fort (2020 Nr. 4 EL-Tagestaxe; vgl. 2021 Nr. 2/4, 2024 Nr. 5, 2025 Nr. 6).

**Nächster Schritt:** Jahrgang 2019 (Nr. 1) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2019 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2019 III Nr. 1** (einziger publizierter Leitentscheid des Jahrgangs):
- Nr. 1 = 5V 18 101 (IV, Invaliditätsbemessung): (1) Reine Homeoffice-Stellen entsprechen (noch) nicht dem ausgeglichenen Arbeitsmarkt nach Art. 16 ATSG; dafür attestierte Arbeitsfähigkeit taugt nicht zur Bemessung des Invalideneinkommens. (2) Teilerwerbstätige ohne Aufgabenbereich: Valideneinkommen analog Art. 27bis Abs. 3 IVV auf Vollpensum hochrechnen, ungewichteten IV-Grad ermitteln, dann mit Erwerbspensum gewichten.

**Neue Seite (1):** [[lgve-2019-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2018), [[index]] (93 Seiten). **Backlink ergänzt:** [[invalideneinkommen]] (direkter Konzept-Treffer).

**Nächster Schritt:** Jahrgang 2018 (Nr. 1–7) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2018 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2018 III Nr. 1–7** (kein Internetentscheid):
- Nr. 1 = 5R 17 1 (Prämienverbilligung, abstrakte Erlassprüfung; Einkommensgrenze Fr. 54'000 für Kinder/junge Erwachsene nicht willkürlich)
- Nr. 2 = 5V 16 505 (IV, Kinderrente Stiefkind: Ausbildung im Ausland → keine Hausgemeinschaft) – LU-Datum 19.01.2018 (Metadatum 07.10.2016 = Verfügung)
- Nr. 3 = 5V 16 373 (AHV, Arbeitnehmerbegriff Art. 10 ATSG einheitlich; mitarbeitende Aktionäre Familien-AG beitragspflichtig; BGer 8C_685/2017)
- Nr. 4 = 5V 17 209 (UVG, Integritätsschaden Zähne: unkorrigierter Zustand massgebend)
- Nr. 5 = 5V 16 469 (IV, Valideneinkommen nach Art. 26 Abs. 1 IVV bei nie verwertbarer Ausbildung; BGer 9C_356/2018) – LU-Datum 19.03.2018 (Metadatum 12.10.2018 = BGer-Datum)
- Nr. 6 = 5V 18 94 und Nr. 7 = 5V 18 35 (Prämienverbilligung: keine nachträgliche Auszahlung; aktuellste Verhältnisse; Anpassung von Amtes wegen § 8a PVG) – inhaltsgleich

**Neue Seite (1):** [[lgve-2018-iii]] (`status: reviewed`), mit Abschnitt «Noch nicht erschlossene Konzepte» (Prämienverbilligung als Konzept-Kandidat – nun 3 Leitentscheide; Kinderrente/Ausbildungsbegriff). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2017), [[index]] (94 Seiten). **Backlinks ergänzt:** [[valideneinkommen]] (Nr. 5), [[plattformarbeit-beitragsstatus]] (Nr. 3 im AHV-Beitrags-Hub), [[uvg-leistungen-revision]] (Nr. 4).

**Lint-Hinweis:** «Prämienverbilligung» (LU PVG/PVV, Art. 65 KVG) ist jetzt durch drei Leitentscheide (2018 Nr. 1/6/7) belegt – eine eigene Konzeptseite ist angezeigt.

**Nächster Schritt:** Jahrgang 2017 (Nr. 1–5) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2017 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2017 III Nr. 1–5** (kein Internetentscheid):
- Nr. 1 = SG 15 2 (KVG-Schiedsgericht; TARMED-Anpassungsverordnung des BR bis Ende 2016 gesetzwidrig, Art. 43 Abs. 4 KVG) – LU-Datum 29.05.2017 (Metadatum 20.06.2014 = Verordnungsdatum; citation_string in opencaselaw leer → nur Canonical-Link)
- Nr. 2 = 5V 16 443 (IV, Hilflosigkeit/lebenspraktische Begleitung; KSIH Rz. 8050.1 unvereinbar mit BGE 133 V 450, unangewendet) – LU-Datum 03.05.2017 (Metadatum 01.01.2015 = KSIH-Fassung)
- Nr. 3 = 5V 16 290 (AHV, Mitarbeiteraktien zu Vorzugsbedingungen = geldwerter Vorteil/massgebender Lohn)
- Nr. 4 = 5V 17 157 (KVG, Wohnung mit Dienstleistung ≠ Pflegeheim; Restfinanzierung Wohnsitzgemeinde)
- Nr. 5 = 5V 17 20 (AHV, WML Rz. 2114.3 nicht rückwirkend auf früheren Sachverhalt) – LU-Datum 27.11.2017 (Metadatum 01.01.2016 = WML-Stichtag)

**Neue Seite (1):** [[lgve-2017-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2016), [[index]] (95 Seiten). **Backlinks/Hub-Ausbau:** [[kvg-wirtschaftlichkeitspruefung]] (neuer Abschnitt als KVG-Anker: 2017 Nr. 1/4, 2021 Nr. 5, 2024 Nr. 9, 2025 Nr. 5), [[hilflosenentschaedigung]] (Nr. 2), [[plattformarbeit-beitragsstatus]] (Nr. 3/5), [[el-pflegeversicherung]] (Nr. 4 + 2021 Nr. 5).

**Beobachtung:** Der «Weisungs-/Verordnungskontrolle»-Strang verdichtet sich weiter: 2017 versagt das KG gleich dreimal einer untergesetzlichen Norm die Anwendung (TARMED-V des BR, KSIH, WML) – konsistent mit 2020 Nr. 4, 2021 Nr. 2/4, 2024 Nr. 5, 2025 Nr. 6. Kandidat für eine eigene Konzeptseite «Verwaltungsweisungen/Normenkontrolle im SVR».

**Nächster Schritt:** Jahrgang 2016 (Nr. 1–9) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2016 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2016 III Nr. 1–9** (kein Internetentscheid):
- Nr. 1 = 5V 15 244 (KVG, Geburtsgebrechen zahnärztl. Leistung über das 20. Altersjahr; BGer 9C_197/2016 NE)
- Nr. 2 = 5V 15 40 (KVG, Augenlidptosis = Leiden mit Krankheitswert)
- Nr. 3 = 5V 16 103 (KVG, Liste säumiger Prämienzahler Art. 64a Abs. 7: nur zahlungsunwillig; erst nach Fortsetzungsbegehren)
- Nr. 4 = 5V 15 445 (IV, MEDAS-Zufallsprinzip Art. 72bis IVV; einvernehmliche Abweichung zulässig; EFL)
- Nr. 5 = 5S 15 1 (Verfahren, Revision nach § 175 VRG ist kostenpflichtig; Art. 61 lit. a ATSG n.a.; BGer 8C_428/2016)
- Nr. 6 = 5V 15 79 (IV, SchlB lit. a: Mahn-/Bedenkzeitverfahren auch beim Abbruch der Eingliederung) – entschieden 09.07.2015, publiziert LGVE 2016
- Nr. 7 = 5V 16 179 (Prämienverbilligung, generelle Aufrechnung Liegenschaftsunterhalt rechtswidrig; § 7 PVG abschliessend)
- Nr. 8 = 5V 15 429 (IV, HE betreutes Wohnen: Heim Art. 35ter IVV vs. eigenes Zuhause)
- Nr. 9 = 5V 14 621 (IV, RAD-Hirnstrommessungen QEEG/ERP keine wissenschaftlich anerkannte Methode)

**Neue Seite (1):** [[lgve-2016-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2015), [[index]] (96 Seiten). **Backlinks ergänzt:** [[suissemedp-zufallsprinzip]] (Nr. 4), [[schlussbestimmungen-6a]] (Nr. 6), [[medizinische-begutachtung]] (Nr. 9/4), [[hilflosenentschaedigung]] (Nr. 8); KVG-Entscheide (Nr. 1–3) über [[kvg-wirtschaftlichkeitspruefung]] angebunden.

**Beobachtung:** Weisungs-/Praxiskontrolle erneut präsent (Nr. 7: rechtswidrige Aufrechnungspraxis). «Prämienverbilligung» nun durch 2016 Nr. 7 + 2018 Nr. 1/6/7 belegt – Konzeptseite weiterhin angezeigt.

**Hinweis Loop:** Cron-Job 1422c663 hat mehrfach hintereinander ausgelöst (gestaute Fires); pro Durchlauf wird nur ein Jahrgang verarbeitet, um Doppelerfassung zu vermeiden.

**Nächster Schritt:** Jahrgang 2015 (Nr. 1–4) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2015 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2015 III Nr. 1–4** (alle IV, kein Internetentscheid):
- Nr. 1 = 5V 13 307 (Rentenrevision Art. 17 ATSG bei rückwirkend abgestufter/befristeter Rente; Anfechtungsgegenstand; Wartezeit Art. 29bis IVV)
- Nr. 2 = 5V 14 10 (geschützter Arbeitseinsatz 70 % kein Unterbruch Art. 29ter IVV; Rentenbeginn Übergangsrecht 5. IV-Revision)
- Nr. 3 = 5V 14 361 (Depression: fehlende konsequente Therapie → kein invalidisierender Charakter)
- Nr. 4 = 5V 14 349 (altrechtliches Gutachten behält Beweiswert im Licht von BGE 141 V 281) – LU-Datum 20.08.2015 (Metadatum/citation 03.06.2015 = Datum von BGE 141 V 281)

**Neue Seite (1):** [[lgve-2015-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2014), [[index]] (97 Seiten). **Backlinks ergänzt:** [[rentenrevision]] (Nr. 1/2), [[depression-invaliditaet]] (Nr. 3), [[bge-141-v-281]] (Nr. 4/3).

**Beobachtung:** Nr. 3 und 4 sind frühe LU-Anwendungen des am 3.6.2015 ergangenen BGE 141 V 281 (Indikatorenprüfung) – sie binden den LGVE-Bestand direkt an den zentralen Schmerzrechtsprechungs-Cluster des Wikis an.

**Nächster Schritt:** Jahrgang 2014 (Nr. 1–5) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2014 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2014 III Nr. 1–5** (kein Internetentscheid):
- Nr. 1 = 5V 13 259 (ALV, Anrechnung im Ausland zurückgelegter Versicherungszeiten; FZA/GVO 883/2004)
- Nr. 2 = 5V 13 157 (KVG/Verfahren, Vergleich Art. 50 ATSG: Aufklärung + Bedenkzeit; faires Verfahren)
- Nr. 3 = S 13 118 (KVG, Hausarztmodell: Verbleib trotz Wohnheim ohne Pflegeabteilung; Gatekeeperfunktion)
- Nr. 4 = 5V 14 185 (IV, unentgeltliche Verbeiständung im Verwaltungsverfahren bei 6a-Revision grundsätzlich erforderlich; Art. 37 Abs. 4 ATSG)
- Nr. 5 = S 13 240 (IV, verbleibende Aktivitätsdauer < 2 Jahre → keine verwertbare Resterwerbsfähigkeit → ganze Rente)

**Neue Seite (1):** [[lgve-2014-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2013), [[index]] (98 Seiten). **Backlinks ergänzt:** [[unentgeltliche-rechtsverbeistaendung]] (Nr. 4 – direkter Treffer), [[verwertbarkeit-restarbeitsfaehigkeit-alter]] (Nr. 5 – direkter Treffer), [[alv-koordination]] (Nr. 1), [[kvg-wirtschaftlichkeitspruefung]] (Nr. 2/3, zugleich 2016 Nr. 1–3 nachgetragen).

**Nächster Schritt:** Jahrgang 2013 (Nr. 1–6) inhaltlich erschliessen.

## [2026-06-13] ingest | LGVE-Jahrgang 2013 inhaltlich erschlossen (opencaselaw lu_gerichte)

Fortsetzung des rückwärtsgerichteten Ingests (`/loop`, Job 1422c663). **Erschlossen: LGVE 2013 III Nr. 1–6** (Übergangsjahr; Nr. 1 noch Verwaltungsgericht, SV-Abt.):
- Nr. 1 = S 11 430 (UVG, Ersatzprämie Art. 95 Abs. 1bis UVG für das ganze Kollektiv geschuldet)
- Nr. 2 = S 12 412 (IV, Assistenzbeitrag: Kriterium «Führen eines eigenen Haushalts» Art. 39b lit. a IVV)
- Nr. 3 = S 12 78 (IV/Verfahren, vorbestehender nicht erkannter Gesundheitsschaden als neue Tatsache § 175 VRG; Kostenfrage offen – später in 2016 Nr. 5 geklärt)
- Nr. 4 = S 12 19 (IV, PTBS → Persönlichkeitsänderung nach Kriegserlebnissen; invalidisierende Wirkung; vor BGE 141 V 281)
- Nr. 5 = S 12 588 (KVG, Pflege-Restfinanzierung: Wohnsitz massgebend; interkantonal Bundesrecht/ZGB, innerkantonal PFG)
- Nr. 6 = S 13 44 (ALV, Leistungsexport Art. 69 VO 1408/71: Aufklärungs-/Beratungspflicht Art. 27 ATSG; Vertrauensschutz)

**Neue Seite (1):** [[lgve-2013-iii]] (`status: reviewed`). **Aktualisiert:** [[lgve-3-abteilung]] (Jahrgangsliste, nächster Schritt 2012 – grösserer Jahrgang mit 19 Entscheiden), [[index]] (99 Seiten). **Backlinks ergänzt:** [[unfall-psyche-hirnverletzung]] (Nr. 4 PTBS), [[hilflosenentschaedigung]] (Nr. 2 Assistenzbeitrag), [[alv-koordination]] (Nr. 6), [[el-pflegeversicherung]] (Nr. 5), [[uvg-leistungen-revision]] (Nr. 1), [[sv-verfahren-besonderheiten]] (Nr. 3).

**Beobachtung:** Mehrere thematische Stränge erhalten ihren frühesten LU-Beleg: Assistenzbeitrag (2013→2023), Pflege-Restfinanzierung (2013→2017→2021), internationale ALV-Koordination (2013→2014), prozessuale Revision (2013→2016). Die Jahresseiten sind über «Hinweis»-Querverweise chronologisch verkettet.

**Nächster Schritt:** Jahrgang 2012 (Nr. 1–21 ohne Nr. 4 und 12 = 19 Entscheide) – voraussichtlich über mehrere Loop-Durchläufe.

## [2026-06-13] lint | Strukturbruch entdeckt: LGVE-Band III ≤2012 ist NICHT Sozialversicherungsrecht

Beim Ansetzen von Jahrgang 2012 (`/loop`, Job 1422c663) festgestellt, dass **sämtliche 19 Einträge LGVE 2012 III nicht sozialversicherungsrechtlich** sind:
- Nr. 1–3 Bürgerrecht/Einbürgerung (Regierungsrat), Nr. 5–11 Ausländerrecht (JSD), Nr. 13–14 Stimm-/Volksrechte (RR), Nr. 15–16 Bildung (BKD), Nr. 17–18 Planungs- und Baurecht (RR), Nr. 19–21 Sozialhilfe (GSD).

**Erklärung:** Vor der Kantonsgerichtsreform (1.6.2013) bezeichnete die LGVE-Bandnummer „III" das **allgemeine Verwaltungsrecht**; das **Sozialversicherungsrecht** stand im **Band II** (Stichprobe: «S 98 624 = LGVE 1999 II Nr. 46», ALV). Erst ab **2013 III** = neue 3. Abteilung KG = SVR.

> WIDERSPRUCH (in [[lgve-3-abteilung]] dokumentiert): «846 SVR-Entscheide 1981–2025» (frühere Annahme) vs. tatsächlich nur **2013–2025 III = SVR** (74 Entscheide); ≤2012 III = Verwaltungsrecht, out of scope. Das pre-2013-SVR (LGVE Band II) ist nicht Teil des raw-Ordners.

**Konsequenz:** Der **SVR-LGVE-Ingest ist abgeschlossen** (13 Jahresseiten 2013–2025). Für Jahrgang 2012 wurde **keine** SVR-Jahresseite angelegt. Index [[lgve-3-abteilung]] um Strukturbruch-Hinweis und Abschlussvermerk ergänzt.

**Offene Benutzerentscheidung:** (a) LGVE-Ingest hier abschliessen (SVR komplett), oder (b) die pre-2013-Bände III (Verwaltungsrecht) trotz fehlendem SVR-Bezug ebenfalls dokumentieren.

## [2026-06-13] lint | Gesundheitsprüfung nach LGVE-SVR-Ingest

Vollständiger Lint über 101 Inhaltsseiten. **Strukturell sehr gesund:** 0 tote Wikilinks, 0 verwaiste Seiten. Befunde:
- 🔴 keine (der einzige strukturelle Widerspruch – LGVE-Band III ≤2012 ≠ SVR – ist in [[lgve-3-abteilung]] als WIDERSPRUCH markiert und aufgelöst).
- 🟡 [[lgve-3-abteilung]] `needs_update` → in diesem Lint auf `reviewed` gesetzt (SVR-Ingest abgeschlossen); [[verfahrensfreie-verfuegung]] weiterhin `draft`; «846 SVR-Entscheide» zu «846 PDF-Einträge» korrigiert.
- 🔵 Konzept-Lücken (mehrfach in LGVE-Jahresseiten referenziert, keine eigene Seite): Prämienverbilligung (4 LE), Kinderrente/Ausbildungsbegriff, Assistenzbeitrag, EO/EOG, Militärversicherung, internationale Koordination.

**Empfohlene neue Artikel:** `praemienverbilligung`, `kinderrente`, `assistenzbeitrag`. Report: [[lint-report-2026-06-13-lgve]].

## [2026-06-13] update | 6 Konzept-Lücken aus dem Lint geschlossen (neue Seiten)

Auf Benutzerwunsch alle im Lint identifizierten Konzept-Lücken als eigene Seiten angelegt (Inhalt aus den erschlossenen LGVE-Entscheiden, opencaselaw `lu_gerichte`):
- [[praemienverbilligung]] (2018 III Nr. 1/6/7, 2016 III Nr. 7)
- [[kinderrente]] (2018 III Nr. 2, 2022 III Nr. 2, 2024 III Nr. 7)
- [[assistenzbeitrag]] (2013 III Nr. 2, 2023 III Nr. 3)
- [[erwerbsersatzordnung]] (2022 III Nr. 1, 2023 III Nr. 4)
- [[militaerversicherung]] (Internetentscheid 2023, 5V 21 350)
- [[internationale-sv-koordination]] (2013 III Nr. 6, 2014 III Nr. 1)

**Vernetzung:** [[index]] um Kategorie «Weitere Sozialversicherungszweige / Querschnitt» ergänzt (→ 105 Themenseiten). Backlinks gesetzt aus [[kvg-wirtschaftlichkeitspruefung]], [[ergaenzungsleistungen]], [[hilflosenentschaedigung]], [[iv-revision-6a]], [[rentenrevision]], [[alv-koordination]], [[uvg-kausalzusammenhang]], [[uvg-leistungen-revision]]. Auf den LGVE-Jahresseiten 2016/2018/2022/2023 die «noch keine Konzeptseite»-Platzhalter durch echte Links ersetzt; «Noch nicht erschlossene Konzepte»-Abschnitte aktualisiert; in 2013/2014/2023 die neuen Konzept-Links nachgetragen.

**Graph-Check nach Anlage:** 0 tote Links, 0 verwaiste Seiten; die 6 neuen Seiten haben je 4–6 eingehende Links. Verbleibende Lücken (geringe Priorität): berufliche Vorsorge/Säule 3a, Witwen-/Witwerrente (Beeler, derzeit in [[egmr-emrk-svr]]).
