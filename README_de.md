# gpt-vis

Ein Python-Wrapper für [gpt-vis-cli](https://github.com/connect-a-sketch/gpt-vis-cli), der die programmgesteuerte und befehlszeilenbasierte Erstellung von Diagrammen ermöglicht.

## Installation

Installieren Sie das Paket mit pip:

```bash
pip install gpt-vis
```

Oder, wenn Sie das Repository geklont haben, können Sie es im bearbeitbaren Modus mit Poetry installieren:

```bash
poetry install
```

## Verwendung

### Als Python-Bibliothek

Sie können `gpt-vis` verwenden, um Diagramme programmgesteuert in Ihren Python-Anwendungen zu erstellen.

```python
from gpt_vis.charts import render_bar_chart, BarChartOptions, BarChartData

# Optionen für ein Balkendiagramm definieren
bar_chart_options = BarChartOptions(
    data=[
        BarChartData(category="A", value=10),
        BarChartData(category="B", value=20),
        BarChartData(category="C", value=15),
    ],
    title="Beispiel-Balkendiagramm",
    axisXTitle="Kategorie",
    axisYTitle="Wert",
)

# Das Balkendiagramm rendern und in einer Datei speichern
render_bar_chart(options=bar_chart_options, output_path="bar_chart.png")
```

### Als Befehlszeilentool

`gpt-vis` bietet auch eine Befehlszeilenschnittstelle für die schnelle Erstellung von Diagrammen.

```bash
gpt-vis '''{"type": "bar", "data": [{"category": "A", "value": 10}, {"category": "B", "value": 20}], "title": "Mein Diagramm"}''' output.png
```

## Verfügbare Diagramme

`gpt-vis` unterstützt eine Vielzahl von Diagrammtypen:

- Fläche
- Balken
- Boxplot
- Säule
- Bezirkskarte
- Doppelachsen
- Fischgrätendiagramm
- Flussdiagramm
- Trichter
- Histogramm
- Linie
- Flüssigkeit
- Mindmap
- Netzwerkdiagramm
- Organigramm
- Pfadkarte
- Kuchen
- Radar
- Sankey
- Streuung
- Treemap
- Venn
- Violine
- Wortwolke

Ausführliche Optionen für jeden Diagrammtyp finden Sie in der Datei `gpt_vis/charts.py`.

## Entwicklung

Um die Tests auszuführen, führen Sie den folgenden Befehl aus:

```bash
poetry run pytest
```

Um die Demo auszuführen, die eine Vielzahl von Diagrammbildern im Verzeichnis `output` generiert:

```bash
poetry run python run.py
```
