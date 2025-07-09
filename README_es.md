# gpt-vis

Un envoltorio de Python para [gpt-vis-cli](https://github.com/connect-a-sketch/gpt-vis-cli), que permite la generación de gráficos de forma programática y desde la línea de comandos.

## Instalación

Instale el paquete usando pip:

```bash
pip install gpt-vis
```

O, si ha clonado el repositorio, puede instalarlo en modo editable usando Poetry:

```bash
poetry install
```

## Uso

### Como biblioteca de Python

Puede usar `gpt-vis` para generar gráficos de forma programática dentro de sus aplicaciones de Python.

```python
from gpt_vis.charts import render_bar_chart, BarChartOptions, BarChartData

# Definir opciones para un gráfico de barras
bar_chart_options = BarChartOptions(
    data=[
        BarChartData(category="A", value=10),
        BarChartData(category="B", value=20),
        BarChartData(category="C", value=15),
    ],
    title="Gráfico de barras de muestra",
    axisXTitle="Categoría",
    axisYTitle="Valor",
)

# Renderizar el gráfico de barras y guardarlo en un archivo
render_bar_chart(options=bar_chart_options, output_path="bar_chart.png")
```

### Como herramienta de línea de comandos

`gpt-vis` también proporciona una interfaz de línea de comandos para la generación rápida de gráficos.

```bash
gpt-vis '''{"type": "bar", "data": [{"category": "A", "value": 10}, {"category": "B", "value": 20}], "title": "Mi gráfico"}''' output.png
```

## Gráficos disponibles

`gpt-vis` admite una amplia variedad de tipos de gráficos:

- Área
- Barra
- Diagrama de caja
- Columna
- Mapa de distrito
- Ejes duales
- Diagrama de espina de pescado
- Diagrama de flujo
- Embudo
- Histograma
- Línea
- Líquido
- Mapa mental
- Gráfico de red
- Organigrama
- Mapa de ruta
- Tarta
- Radar
- Sankey
- Dispersión
- Mapa de árbol
- Venn
- Violín
- Nube de palabras

Para obtener opciones detalladas para cada tipo de gráfico, consulte el archivo `gpt_vis/charts.py`.

## Desarrollo

Para ejecutar las pruebas, ejecute el siguiente comando:

```bash
poetry run pytest
```

Para ejecutar la demostración, que genera una variedad de imágenes de gráficos en el directorio `output`:

```bash
poetry run python run.py
```
