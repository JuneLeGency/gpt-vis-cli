# gpt-vis

一个用于 [gpt-vis-cli](https://github.com/connect-a-sketch/gpt-vis-cli) 的 Python 封装，支持通过编程和命令行方式生成图表。

## 安装

使用 pip 安装：

```bash
pip install gpt-vis
```

或者，如果您已经克隆了代码仓库，可以使用 Poetry 以可编辑模式安装：

```bash
poetry install
```

## 使用方法

### 作为 Python 库

您可以在您的 Python 应用程序中以编程方式使用 `gpt-vis` 生成图表。

```python
from gpt_vis.charts import render_bar_chart, BarChartOptions, BarChartData

# 定义柱状图的选项
bar_chart_options = BarChartOptions(
    data=[
        BarChartData(category="A", value=10),
        BarChartData(category="B", value=20),
        BarChartData(category="C", value=15),
    ],
    title="示例柱状图",
    axisXTitle="类别",
    axisYTitle="数值",
)

# 渲染柱状图并保存到文件
render_bar_chart(options=bar_chart_options, output_path="bar_chart.png")
```

### 作为命令行工具

`gpt-vis` 也提供了一个命令行界面，用于快速生成图表。

```bash
gpt-vis '''{"type": "bar", "data": [{"category": "A", "value": 10}, {"category": "B", "value": 20}], "title": "我的图表"}''' output.png
```

## 可用图表类型

`gpt-vis` 支持多种图表类型：

- 面积图 (Area)
- 条形图 (Bar)
- 箱线图 (Boxplot)
- 柱状图 (Column)
- 行政区划地图 (District Map)
- 双轴图 (Dual Axes)
- 鱼骨图 (Fishbone Diagram)
- 流程图 (Flow Diagram)
- 漏斗图 (Funnel)
- 直方图 (Histogram)
- 折线图 (Line)
- 水波图 (Liquid)
- 思维导图 (Mind Map)
- 网络图 (Network Graph)
- 组织结构图 (Organization Chart)
- 路径地图 (Path Map)
- 饼图 (Pie)
- 雷达图 (Radar)
- 桑基图 (Sankey)
- 散点图 (Scatter)
- 矩形树图 (Treemap)
- 韦恩图 (Venn)
- 小提琴图 (Violin)
- 词云图 (Word Cloud)

有关每种图表类型的详细选项，请参阅 `gpt_vis/charts.py` 文件。

## 开发

要运行测试，请执行以下命令：

```bash
poetry run pytest
```

要运行演示，该演示会在 `output` 目录中生成各种图表图像：

```bash
poetry run python run.py
```
