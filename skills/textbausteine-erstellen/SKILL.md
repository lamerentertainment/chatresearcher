---
name: textbausteine-erstellen
description: Erstelle gerichtskonforme Textbausteine zur abstrakten Rechtslage (Tatbestand + Rechtsprechung) nach selbständiger Recherche via OpenCaseLaw MCP. Verwende für Anfragen wie "Textbaustein zu Art. X StGB", "Rechtslage zu ...", "Erstelle einen Baustein zu ...".
---

# Skill: Textbaustein via OpenCaseLaw erstellen

## Zweck

Dieser Skill leitet Claude an, auf Anfrage selbständig via **OpenCaseLaw MCP** die aktuelle Rechtsprechung zu einem Tatbestand oder einer Rechtsfrage zu recherchieren und das Ergebnis als gerichtskonformen Textbaustein aufzubereiten. Der Textbaustein beschreibt die **abstrakte Rechtslage** – gesetzlicher Tatbestand und einschlägige Rechtsprechung – ohne Subsumtion auf einen konkreten Sachverhalt.

---

## 1. Arbeitsablauf

### Schritt 0 – Bestehende Textbausteine prüfen

Bevor Claude mit der Recherche beginnt, liest er **zuerst die Indexdatei** `skills/textbausteine-erstellen/resources/tb/index.md`. Diese Datei listet alle verfügbaren Textbausteine mit Kürzel, Titel und Dateiname auf und ist der schnellste Weg zu prüfen, ob ein Baustein bereits existiert.

1. **Existiert bereits ein Baustein** für den angefragten Artikel? Index prüfen, dann:
   - Den bestehenden Baustein dem Benutzer vorlegen (Datei lesen und Inhalt zeigen).
   - Fragen, ob er aktualisiert, ergänzt oder ein neuer Baustein daneben erstellt werden soll.
   - Keinen neuen Baustein erstellen, ohne dies zu klären.

2. **Bestehende Bausteine als Vorlage nutzen**: Claude liest 1–2 thematisch verwandte Bausteine aus dem Index (gleicher Gesetzesabschnitt, ähnliche Struktur), um Stil, Detailtiefe und Aufbau konsistent zu halten.

Die Dateinamen folgen dem Schema `[Gesetz][Artikel][Suffix].md` (z.B. `StGB146.md`, `StGB146a.md`, `StGB146b.md`). Varianten eines Artikels (Absätze, Qualifikationen) werden als separate Dateien mit Suffix angelegt. **Nach dem Erstellen eines neuen Bausteins ist der Index zu aktualisieren.**

### Schritt 1 – Recherche (ohne Rückfrage sofort starten)

Claude wählt die OpenCaseLaw-Tools nach Fragestellung:

| Situation | Tool |
|---|---|
| Leitentscheide zu einem Gesetzesartikel | `get_doctrine` (primär), ergänzend `find_leading_cases` |
| Rechtsprechung zu einer Rechtsfrage | `search_decisions` mit präzisem Suchbegriff |
| Bestimmten Entscheid prüfen | `get_case_brief` (Kurzfassung) oder `get_decision` (Volltext) |
| Aktualität eines BGE prüfen | `find_citations` oder `analyze_legal_trend` |
| Gesetzestext nachschlagen | `get_law` (SR-Nummer) oder `search_laws` |

Claude kombiniert mehrere Tools, wenn nötig (z.B. zuerst `get_doctrine`, dann `get_case_brief` für die relevantesten Treffer).

### Schritt 2 – Ergebnisse sichten

- Ist der Entscheid **einschlägig** (betrifft er den angefragten Tatbestand)?
- Ist der Entscheid **aktuell** (nicht durch neuere Rechtsprechung überholt)?
- **Instanzhierarchie**: BGE vor nicht publizierten BGer-Urteilen; publizierte vor nicht publizierten Entscheiden.

### Schritt 3 – Textbaustein formulieren (gemäss Abschnitt 2 und 3)

---

## 2. Aufbau des Textbausteins

### 2.1 Struktur

1. **Gesetzlicher Tatbestand**: Sinngemässe Umschreibung der einschlägigen Norm(en). Kein wörtliches Abschreiben des Gesetzestexts, sondern eigene Formulierung.
2. **Objektiver Tatbestand**: Darstellung der Tatbestandselemente mit einschlägiger Rechtsprechung.
3. **Subjektiver Tatbestand**: Vorsatzanforderungen, Absicht oder besondere subjektive Merkmale mit Rechtsprechung.
4. *(Fakultativ)* **Qualifikationen, Privilegierungen, Konkurrenzen**: Falls sachlich geboten oder vom Benutzer verlangt.

Der Textbaustein enthält **keine Subsumtion** und **kein Ergebnis zum konkreten Fall** – es sei denn, der Benutzer verlangt dies ausdrücklich.

### 2.2 Sprache

- **Fliesstext** ohne Aufzählungspunkte, Nummerierungen oder Hervorhebungen (kein Fettdruck, keine Kursivschrift).
- **Indikativ Präsens** für geltende Rechtslage und für die Wiedergabe von Bundesgerichtsrechtsprechung. Kein Konjunktiv bei BGE-Wiedergabe (es sind geltende Rechtsauffassungen, keine Drittmeinungen).
- **Sachlich, präzise, nüchtern**. Keine wertenden Formulierungen.
- **Schweizerische Rechtschreibung** (ss statt ß).
- **Quellenangaben in Klammern am Satzende**, damit der Lesefluss nicht unterbrochen wird.
- **Keine wörtlichen Zitate** aus Entscheiden im Fliesstext. Ausnahme: Prägnante, eingebürgerte Kurzformeln dürfen in Anführungszeichen wiedergegeben werden.

### 2.3 Einleitungsformeln

Für den gesetzlichen Tatbestand:
> Nach Art. XX [Abs. X] StGB …
> Gemäss Art. XX StGB …

Für Rechtsprechungshinweise:
> Das Bundesgericht hat dazu festgehalten, dass … (BGE XX IV XXX E. X.X).
> Nach ständiger Rechtsprechung des Bundesgerichts … (BGE XX IV XXX E. X.X; BGer-Urteil XB_XXX/20XX vom XX.XX.20XX E. X.X).

---

## 3. Zitierweise

Keine Hyperlinks im Textbaustein (direkte Verwendung im Urteil muss möglich sein). Biete dem User aber in einem 
begleitenden Text Hyperlinks an, damit er die verwendeten Zitate prüfen kann.

### 3.1 BGE
```
BGE 134 IV 82 E. 6.2.1
BGE 137 II 321 E. 2a
```
Seitenangabe (S. xx) ist fakultativ. Mehrere BGE aus derselben Quelle durch Komma getrennt.

### 3.2 Nicht publizierte BGer-Urteile
```
BGer-Urteil 6B_401/2007 vom 08.11.2007 E. 3.3
```

### 3.3 Kantonale Urteile
```
Urteil des Kantonsgerichts Luzern 3B 13 2 vom 01.08.2013 E. 2
KrG-Urteil 2O6 13 2 vom 19.09.2008
```

### 3.4 Reihenfolge innerhalb der Klammer
1. Höhere Instanz vor tieferer Instanz.
2. Publizierte vor nicht publizierten Entscheiden (Trennung durch Strichpunkt).
3. Jüngerer Entscheid vor älterem.

Beispiel: `(BGE 147 IV 73 E. 3.1, 133 IV 207 E. 4.2; BGer-Urteil 6B_401/2021 vom 08.11.2021 E. 3.3)`

### 3.5 Gesetze
Geläufige Gesetze (StGB, StPO, BetmG, SVG, WG, AIG) brauchen beim erstmaligen Zitat keine Langform. Bei weniger geläufigen Gesetzen: Gesetzestitel ausschreiben mit Abkürzung und SR-Nummer in Klammern, danach nur noch Abkürzung. Beispiel: `Tierschutzgesetz (TSchG; SR 455)`

---

## 4. Ausgabeformat

Der fertige Textbaustein wird **immer** in folgendem Format ausgegeben:

```
[Artikelkürzel]	[Kurztitel]

#Beginn [Artikelkürzel] [Kurztitel]#[Fliesstext des Bausteins]#Ende [Artikelkürzel]#

hinzugefügt am [Datum im Format TT.MM.JJJJ]
```

**Beispiel:**

```
StGB146	Betrug

#Beginn StGB146 Betrug#Gemäss Art. 146 Abs. 1 StGB macht sich des Betruges schuldig, wer in der Absicht, sich oder einen andern unrechtmässig zu bereichern, jemanden durch Vorspiegelung oder Unterdrückung von Tatsachen arglistig irreführt oder ihn in einem Irrtum arglistig bestärkt und so den Irrenden zu einem Verhalten bestimmt, wodurch dieser sich selbst oder einen andern am Vermögen schädigt. Der Tatbestand setzt in objektiver Hinsicht eine arglistige Täuschung, einen dadurch hervorgerufenen oder aufrechterhaltenen Irrtum, eine Vermögensdisposition des Getäuschten und einen Vermögensschaden voraus, wobei zwischen diesen Elementen ein Motivationszusammenhang bestehen muss. Arglist liegt nach der Rechtsprechung vor, wenn der Täter ein ganzes Lügengebäude errichtet oder sich besonderer Machenschaften oder Kniffe bedient. Einfache falsche Angaben gelten als arglistig, wenn deren Überprüfung nicht oder nur mit besonderer Mühe möglich oder nicht zumutbar ist, sowie dann, wenn der Täter den Getäuschten von der möglichen Überprüfung abhält oder nach den Umständen voraussieht, dass dieser die Überprüfung aufgrund eines besonderen Vertrauensverhältnisses unterlassen werde (BGE 147 IV 73 E. 3.1; 142 IV 153 E. 2.2.2; 135 IV 76 E. 5.2). In subjektiver Hinsicht verlangt Art. 146 Abs. 1 StGB Vorsatz hinsichtlich aller objektiver Tatbestandsmerkmale sowie die Absicht unrechtmässiger Bereicherung. Eventualvorsatz genügt, ausgenommen bezüglich der Bereicherungsabsicht, die als überschiessende Innentendenz direkten Vorsatz erfordert (BGE 134 IV 210 E. 5.3).#Ende StGB146#

hinzugefügt am 28.03.2026
```

---

## 5. Qualitätssicherung

- **Aktualität**: Via `find_citations` oder `analyze_legal_trend` prüfen, ob zitierte Entscheide noch massgeblich sind. Überholte Rechtsprechung wird nicht verwendet.
- **Keine Halluzinationen**: Claude erfindet keine BGE-Nummern und keine Erwägungsziffern. Wenn die Recherche keine einschlägige Rechtsprechung ergibt, wird dies mitgeteilt, anstatt Quellen zu fabrizieren.
- **Keine langen Urteilszitate**: Der Textbaustein gibt die Rechtsprechung sinngemäss wieder.
- **Einheitliche Terminologie**: Durchgängig dieselben Begriffe verwenden (z.B. konsequent "beschuldigte Person" oder "Beschuldigter").
- **Hinweis an Benutzer**: Claude weist am Ende darauf hin, dass die Einschlägigkeit und Aktualität der zitierten Entscheide vom Gerichtsschreiber zu prüfen sind.
