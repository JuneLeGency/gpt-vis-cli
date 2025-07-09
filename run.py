from gpt_vis_python import render_chart, AreaChartOptions, BarChartOptions
from gpt_vis_python.charts import render_area_chart, render_bar_chart

options = AreaChartOptions(
    width=600,
    height=400,
    data=[
        {'time': '1991', 'value': 3},
        {'time': '1992', 'value': 4},
        {'time': '1993', 'value': 3.5},
        {'time': '1994', 'value': 5},
        {'time': '1995', 'value': 4.9},
        {'time': '1996', 'value': 6},
        {'time': '1997', 'value': 7},
        {'time': '1998', 'value': 9},
        {'time': '1999', 'value': 13},
    ],
    axisXTitle='Time',
    axisYTitle='Value',
    title='Area Chart',
)

render_area_chart(options, "area.png")
"""
{
      width: 600,
      height: 400,
      type: 'bar',
      data: [
        { category: 'Sports', value: 275 },
        { category: 'Strategy', value: 115 },
        { category: 'Action', value: 120 },
        { category: 'Shooter', value: 350 },
        { category: 'Other', value: 150 },
      ],
      axisXTitle: 'Type',
      axisYTitle: 'Sold',
      a: 1,
      texture: 'rough',
    }
"""
options = BarChartOptions(
    width=600,
    height=400,
    data=[
        {"category": 'Sports', "value": 275},
        {"category": 'Strategy', "value": 115},
        {"category": 'Action', "value": 120},
        {"category": 'Shooter', "value": 350},
        {"category": 'Other', "value": 150},
    ],
    axisXTitle='Type',
    axisYTitle='Sold',
    a=1,
    texture='rough',
)
render_bar_chart(options, "bar.png")
