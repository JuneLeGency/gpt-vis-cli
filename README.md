# gpt-vis

A Python wrapper for gpt-vis-cli.

## Installation

```bash
poetry install
```

## Usage

```python
from gpt_vis_python import render_chart, BarChartOptions

options = BarChartOptions(
    data=[
        {"category": "A", "value": 10},
        {"category": "B", "value": 20},
    ],
    title="My Bar Chart",
)

render_chart("bar", options, "bar_chart.png")
```