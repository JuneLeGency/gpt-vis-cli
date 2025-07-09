# gpt-vis

Un wrapper Python pour [gpt-vis-cli](https://github.com/connect-a-sketch/gpt-vis-cli), permettant la génération de graphiques par programme et en ligne de commande.

## Installation

Installez le package à l'aide de pip :

```bash
pip install gpt-vis
```

Ou, si vous avez cloné le référentiel, vous pouvez l'installer en mode modifiable à l'aide de Poetry :

```bash
poetry install
```

## Utilisation

### En tant que bibliothèque Python

Vous pouvez utiliser `gpt-vis` pour générer des graphiques par programme dans vos applications Python.

```python
from gpt_vis.charts import render_bar_chart, BarChartOptions, BarChartData

# Définir les options pour un graphique à barres
bar_chart_options = BarChartOptions(
    data=[
        BarChartData(category="A", value=10),
        BarChartData(category="B", value=20),
        BarChartData(category="C", value=15),
    ],
    title="Exemple de graphique à barres",
    axisXTitle="Catégorie",
    axisYTitle="Valeur",
)

# Rendre le graphique à barres et l'enregistrer dans un fichier
render_bar_chart(options=bar_chart_options, output_path="bar_chart.png")
```

### En tant qu'outil de ligne de commande

`gpt-vis` fournit également une interface de ligne de commande pour la génération rapide de graphiques.

```bash
gpt-vis '''{"type": "bar", "data": [{"category": "A", "value": 10}, {"category": "B", "value": 20}], "title": "Mon graphique"}''' output.png
```

## Graphiques disponibles

`gpt-vis` prend en charge une grande variété de types de graphiques :

- Aire
- Barre
- Boîte à moustaches
- Colonne
- Carte de district
- Axes doubles
- Diagramme en arêtes de poisson
- Diagramme de flux
- Entonnoir
- Histogramme
- Ligne
- Liquide
- Carte mentale
- Graphe de réseau
- Organigramme
- Carte de chemin
- Tarte
- Radar
- Sankey
- Dispersion
- Treemap
- Venn
- Violon
- Nuage de mots

Pour des options détaillées pour chaque type de graphique, veuillez vous référer au fichier `gpt_vis/charts.py`.

## Développement

Pour exécuter les tests, exécutez la commande suivante :

```bash
poetry run pytest
```

Pour exécuter la démo, qui génère une variété d'images de graphiques dans le répertoire `output` :

```bash
poetry run python run.py
```
