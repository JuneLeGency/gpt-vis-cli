from gpt_vis.charts import (
    AreaChartOptions,
    BarChartOptions,
    BoxPlotOptions,
    ColumnChartOptions,
    DistrictMapOptions,
    DualAxesOptions,
    FishboneDiagramOptions,
    FlowDiagramOptions,
    FunnelChartOptions,
    HistogramOptions,
    LineChartOptions,
    LiquidChartOptions,
    MindMapOptions,
    NetworkGraphOptions,
    OrganizationChartOptions,
    PathMapOptions,
    PieChartOptions,
    PinMapOptions,
    RadarChartOptions,
    SankeyChartOptions,
    ScatterChartOptions,
    TreemapChartOptions,
    VennChartOptions,
    ViolinPlotOptions,
    WordCloudChartOptions,
    render_area_chart,
    render_bar_chart,
    render_boxplot_chart,
    render_column_chart,
    render_district_map_chart,
    render_dual_axes_chart,
    render_fishbone_diagram_chart,
    render_flow_diagram_chart,
    render_funnel_chart,
    render_histogram_chart,
    render_line_chart,
    render_liquid_chart,
    render_mind_map_chart,
    render_network_graph_chart,
    render_organization_chart,
    render_path_map_chart,
    render_pie_chart,
    render_pin_map_chart,
    render_radar_chart,
    render_sankey_chart,
    render_scatter_chart,
    render_treemap_chart,
    render_venn_chart,
    render_violin_chart,
    render_word_cloud_chart,
)

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

render_area_chart(options, "output/area.png")

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
    texture='rough',
)
render_bar_chart(options, "output/bar.png")

options = BoxPlotOptions(
    data=[
        {
            "category": 'Adelie',
            "value": 181,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 195,
        },
        {
            "category": 'Adelie',
            "value": 191,
        },
        {
            "category": 'Adelie',
            "value": 198,
        },
        {
            "category": 'Adelie',
            "value": 197,
        },
        {
            "category": 'Adelie',
            "value": 194,
        },
        {
            "category": 'Adelie',
            "value": 180,
        },
        {
            "category": 'Adelie',
            "value": 185,
        },
        {
            "category": 'Adelie',
            "value": 180,
        },
        {
            "category": 'Adelie',
            "value": 183,
        },
        {
            "category": 'Adelie',
            "value": 180,
        },
        {
            "category": 'Adelie',
            "value": 178,
        },
        {
            "category": 'Adelie',
            "value": 184,
        },
        {
            "category": 'Adelie',
            "value": 196,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 184,
        },
        {
            "category": 'Adelie',
            "value": 195,
        },
        {
            "category": 'Adelie',
            "value": 196,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 182,
        },
        {
            "category": 'Adelie',
            "value": 191,
        },
        {
            "category": 'Adelie',
            "value": 188,
        },
        {
            "category": 'Adelie',
            "value": 200,
        },
        {
            "category": 'Adelie',
            "value": 191,
        },
        {
            "category": 'Adelie',
            "value": 193,
        },
        {
            "category": 'Adelie',
            "value": 194,
        },
        {
            "category": 'Adelie',
            "value": 195,
        },
        {
            "category": 'Adelie',
            "value": 192,
        },
        {
            "category": 'Adelie',
            "value": 192,
        },
        {
            "category": 'Adelie',
            "value": 188,
        },
        {
            "category": 'Adelie',
            "value": 198,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 197,
        },
        {
            "category": 'Adelie',
            "value": 195,
        },
        {
            "category": 'Adelie',
            "value": 184,
        },
        {
            "category": 'Adelie',
            "value": 195,
        },
        {
            "category": 'Adelie',
            "value": 196,
        },
        {
            "category": 'Adelie',
            "value": 193,
        },
        {
            "category": 'Adelie',
            "value": 194,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 189,
        },
        {
            "category": 'Adelie',
            "value": 205,
        },
        {
            "category": 'Adelie',
            "value": 186,
        },
        {
            "category": 'Adelie',
            "value": 208,
        },
        {
            "category": 'Adelie',
            "value": 196,
        },
        {
            "category": 'Adelie',
            "value": 192,
        },
        {
            "category": 'Adelie',
            "value": 203,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 184,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 197,
        },
        {
            "category": 'Adelie',
            "value": 191,
        },
        {
            "category": 'Adelie',
            "value": 197,
        },
        {
            "category": 'Adelie',
            "value": 196,
        },
        {
            "category": 'Adelie',
            "value": 199,
        },
        {
            "category": 'Adelie',
            "value": 189,
        },
        {
            "category": 'Adelie',
            "value": 198,
        },
        {
            "category": 'Adelie',
            "value": 202,
        },
        {
            "category": 'Adelie',
            "value": 199,
        },
        {
            "category": 'Adelie',
            "value": 195,
        },
        {
            "category": 'Adelie',
            "value": 210,
        },
        {
            "category": 'Adelie',
            "value": 197,
        },
        {
            "category": 'Adelie',
            "value": 199,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 200,
        },
        {
            "category": 'Adelie',
            "value": 193,
        },
        {
            "category": 'Adelie',
            "value": 187,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 185,
        },
        {
            "category": 'Adelie',
            "value": 190,
        },
        {
            "category": 'Adelie',
            "value": 193,
        },
        {
            "category": 'Adelie',
            "value": 201,
        },
        {
            "category": 'Chinstrap',
            "value": 196,
        },
        {
            "category": 'Chinstrap',
            "value": 193,
        },
        {
            "category": 'Chinstrap',
            "value": 197,
        },
        {
            "category": 'Chinstrap',
            "value": 197,
        },
        {
            "category": 'Chinstrap',
            "value": 198,
        },
        {
            "category": 'Chinstrap',
            "value": 194,
        },
        {
            "category": 'Chinstrap',
            "value": 201,
        },
        {
            "category": 'Chinstrap',
            "value": 201,
        },
        {
            "category": 'Chinstrap',
            "value": 197,
        },
        {
            "category": 'Chinstrap',
            "value": 195,
        },
        {
            "category": 'Chinstrap',
            "value": 191,
        },
        {
            "category": 'Chinstrap',
            "value": 193,
        },
        {
            "category": 'Chinstrap',
            "value": 197,
        },
        {
            "category": 'Chinstrap',
            "value": 200,
        },
        {
            "category": 'Chinstrap',
            "value": 205,
        },
        {
            "category": 'Chinstrap',
            "value": 201,
        },
        {
            "category": 'Chinstrap',
            "value": 203,
        },
        {
            "category": 'Chinstrap',
            "value": 195,
        },
        {
            "category": 'Chinstrap',
            "value": 210,
        },
        {
            "category": 'Chinstrap',
            "value": 205,
        },
        {
            "category": 'Chinstrap',
            "value": 210,
        },
        {
            "category": 'Chinstrap',
            "value": 196,
        },
        {
            "category": 'Chinstrap',
            "value": 201,
        },
        {
            "category": 'Chinstrap',
            "value": 212,
        },
        {
            "category": 'Chinstrap',
            "value": 187,
        },
        {
            "category": 'Chinstrap',
            "value": 201,
        },
        {
            "category": 'Chinstrap',
            "value": 203,
        },
        {
            "category": 'Chinstrap',
            "value": 197,
        },
        {
            "category": 'Chinstrap',
            "value": 203,
        },
        {
            "category": 'Chinstrap',
            "value": 202,
        },
        {
            "category": 'Chinstrap',
            "value": 206,
        },
        {
            "category": 'Chinstrap',
            "value": 207,
        },
        {
            "category": 'Chinstrap',
            "value": 193,
        },
        {
            "category": 'Chinstrap',
            "value": 210,
        },
        {
            "category": 'Gentoo',
            "value": 230,
        },
        {
            "category": 'Gentoo',
            "value": 218,
        },
        {
            "category": 'Gentoo',
            "value": 215,
        },
        {
            "category": 'Gentoo',
            "value": 219,
        },
        {
            "category": 'Gentoo',
            "value": 215,
        },
        {
            "category": 'Gentoo',
            "value": 216,
        },
        {
            "category": 'Gentoo',
            "value": 213,
        },
        {
            "category": 'Gentoo',
            "value": 217,
        },
        {
            "category": 'Gentoo',
            "value": 221,
        },
        {
            "category": 'Gentoo',
            "value": 222,
        },
        {
            "category": 'Gentoo',
            "value": 218,
        },
        {
            "category": 'Gentoo',
            "value": 215,
        },
        {
            "category": 'Gentoo',
            "value": 215,
        },
        {
            "category": 'Gentoo',
            "value": 215,
        },
        {
            "category": 'Gentoo',
            "value": 220,
        },
        {
            "category": 'Gentoo',
            "value": 222,
        },
        {
            "category": 'Gentoo',
            "value": 230,
        },
        {
            "category": 'Gentoo',
            "value": 220,
        },
        {
            "category": 'Gentoo',
            "value": 219,
        },
        {
            "category": 'Gentoo',
            "value": 208,
        },
        {
            "category": 'Gentoo',
            "value": 225,
        },
        {
            "category": 'Gentoo',
            "value": 216,
        },
        {
            "category": 'Gentoo',
            "value": 222,
        },
        {
            "category": 'Gentoo',
            "value": 225,
        },
        {
            "category": 'Gentoo',
            "value": 215,
        },
        {
            "category": 'Gentoo',
            "value": 220,
        },
        {
            "category": 'Gentoo',
            "value": 225,
        },
        {
            "category": 'Gentoo',
            "value": 220,
        },
        {
            "category": 'Gentoo',
            "value": 220,
        },
        {
            "category": 'Gentoo',
            "value": 224,
        },
        {
            "category": 'Gentoo',
            "value": 221,
        },
        {
            "category": 'Gentoo',
            "value": 231,
        },
        {
            "category": 'Gentoo',
            "value": 230,
        },
        {
            "category": 'Gentoo',
            "value": 229,
        },
        {
            "category": 'Gentoo',
            "value": 223,
        },
        {
            "category": 'Gentoo',
            "value": 221,
        },
        {
            "category": 'Gentoo',
            "value": 221,
        },
        {
            "category": 'Gentoo',
            "value": 230,
        },
        {
            "category": 'Gentoo',
            "value": 220,
        },
        {
            "category": 'Gentoo',
            "value": 223,
        },
        {
            "category": 'Gentoo',
            "value": 221,
        },
        {
            "category": 'Gentoo',
            "value": 224,
        },
        {
            "category": 'Gentoo',
            "value": 228,
        },
        {
            "category": 'Gentoo',
            "value": 218,
        },
        {
            "category": 'Gentoo',
            "value": 230,
        },
        {
            "category": 'Gentoo',
            "value": 228,
        },
        {
            "category": 'Gentoo',
            "value": 224,
        },
        {
            "category": 'Gentoo',
            "value": 226,
        },
        {
            "category": 'Gentoo',
            "value": 216,
        },
        {
            "category": 'Gentoo',
            "value": 225,
        },
        {
            "category": 'Gentoo',
            "value": 228,
        },
        {
            "category": 'Gentoo',
            "value": 228,
        },
        {
            "category": 'Gentoo',
            "value": 215,
        },
        {
            "category": 'Gentoo',
            "value": 219,
        },
        {
            "category": 'Gentoo',
            "value": 209,
        },
        {
            "category": 'Gentoo',
            "value": 229,
        },
        {
            "category": 'Gentoo',
            "value": 230,
        },
        {
            "category": 'Gentoo',
            "value": 230,
        },
        {
            "category": 'Gentoo',
            "value": 222,
        },
        {
            "category": 'Gentoo',
            "value": 222,
        },
        {
            "category": 'Gentoo',
            "value": 213,
        },
    ],
    width=600,
    height=400,
    axisXTitle='category',
    axisYTitle='value'
)

render_boxplot_chart(options, "output/boxplot.png")

options = ColumnChartOptions(
    data=[
        {"category": "Jan", "value": 62, "group": "Email"},
        {"category": "Jan", "value": 38, "group": "Affiliate"},
        {"category": "Feb", "value": 45, "group": "Email"},
        {"category": "Feb", "value": 28, "group": "Affiliate"},
        {"category": "Mar", "value": 78, "group": "Email"},
        {"category": "Mar", "value": 48, "group": "Affiliate"},
        {"category": "Apr", "value": 68, "group": "Email"},
        {"category": "Apr", "value": 38, "group": "Affiliate"},
        {"category": "May", "value": 48, "group": "Email"},
        {"category": "May", "value": 28, "group": "Affiliate"},
        {"category": "Jun", "value": 38, "group": "Email"},
        {"category": "Jun", "value": 18, "group": "Affiliate"},
    ],
    stack=True,
    group=False,
    width=600,
    height=400,
    axisXTitle="Month",
    axisYTitle="Value",
    title="Monthly Sales Data (Stacked)",
)
render_column_chart(options, "output/column.png")

options = DualAxesOptions(
    categories=['2015', '2016', '2017', '2018', '2019'],
    series=[
        {'type': 'column', 'data': [91.9, 99.1, 101.6, 114.4, 121], 'axisYTitle': 'Sales'},
        {'type': 'line', 'data': [0.055, 0.06, 0.062, 0.07, 0.075], 'axisYTitle': 'Profit Margin'}
    ],
    width=600,
    height=400,
    title='Sales and Profit Margin Over Years',
    axisXTitle='Year'
)
render_dual_axes_chart(options, "output/dual-axes.png")

options = FishboneDiagramOptions(
    data={
        "name": "Quality Issues",
        "children": [
            {
                "name": "Man",
                "children": [
                    {"name": "Lack of Training"},
                    {"name": "Fatigue"},
                ],
            },
            {
                "name": "Machine",
                "children": [
                    {"name": "Aging Equipment"},
                    {"name": "Improper Setup"},
                ],
            },
            {
                "name": "Material",
                "children": [
                    {"name": "Substandard Raw Materials"},
                    {"name": "Incorrect Specifications"},
                ],
            },
            {
                "name": "Method",
                "children": [
                    {"name": "Inconsistent Processes"},
                    {"name": "Lack of Clear Instructions"},
                ],
            },
        ],
    },
    width=800,
    height=600,
)
render_fishbone_diagram_chart(options, "output/fishbone-diagram.png")

options = FlowDiagramOptions(
    data={
        "nodes": [
            {"name": "Start"},
            {"name": "Process 1"},
            {"name": "Process 2"},
            {"name": "End"},
        ],
        "edges": [
            {"source": "Start", "target": "Process 1", "name": "to p1"},
            {"source": "Process 1", "target": "Process 2", "name": "to p2"},
            {"source": "Process 2", "target": "End", "name": "to end"},
        ],
    },
    width=600,
    height=400,
)
render_flow_diagram_chart(options, "output/flow-diagram.png")

options = FunnelChartOptions(
    data=[
        {'category': 'Website Visits', 'value': 50000},
        {'category': 'Added to Cart', 'value': 35000},
        {'category': 'Placed Order', 'value': 25000},
        {'category': 'Paid', 'value': 15000},
        {'category': 'Completed Transaction', 'value': 8000},
    ],
    width=600,
    height=400,
    title='Sales Funnel'
)
render_funnel_chart(options, "output/funnel.png")

options = HistogramOptions(
    data=[78, 88, 60, 100, 95, 85, 75, 65, 90, 80, 70, 60, 100],
    binNumber=5,
    width=600,
    height=400,
    title='Distribution of Scores',
    axisXTitle='Score',
    axisYTitle='Frequency'
)
render_histogram_chart(options, "output/histogram.png")

options = LineChartOptions(
    data=[
        {'time': '2015', 'value': 23},
        {'time': '2016', 'value': 35},
        {'time': '2017', 'value': 45},
        {'time': '2018', 'value': 58},
        {'time': '2019', 'value': 72},
    ],
    width=600,
    height=400,
    title='Growth Over Years',
    axisXTitle='Year',
    axisYTitle='Value'
)
render_line_chart(options, "output/line.png")

options = LiquidChartOptions(
    percent=0.75,
    shape='circle',
    width=400,
    height=400,
    title='Progress Completion'
)
render_liquid_chart(options, "output/liquid.png")

options = MindMapOptions(
    data={
        "name": "Central Topic",
        "children": [
            {"name": "Main Topic 1"},
            {"name": "Main Topic 2"},
            {"name": "Main Topic 3"},
        ],
    },
    width=600,
    height=400,
)
render_mind_map_chart(options, "output/mind-map.png")

options = NetworkGraphOptions(
    data={
        "nodes": [
            {"name": "A"},
            {"name": "B"},
            {"name": "C"},
            {"name": "D"},
        ],
        "edges": [
            {"source": "A", "target": "B"},
            {"source": "A", "target": "C"},
            {"source": "B", "target": "D"},
        ],
    },
    width=600,
    height=400,
)
render_network_graph_chart(options, "output/network-graph.png")

options = OrganizationChartOptions(
    data={
        "name": "CEO",
        "children": [
            {
                "name": "VP of Engineering",
                "children": [
                    {"name": "Team Lead 1"},
                    {"name": "Team Lead 2"},
                ],
            },
            {
                "name": "VP of Sales",
                "children": [
                    {"name": "Sales Manager 1"},
                    {"name": "Sales Manager 2"},
                ],
            },
        ],
    },
    width=800,
    height=600,
)
render_organization_chart(options, "output/organization-chart.png")

options = PieChartOptions(
    data=[
        {'category': 'Category A', 'value': 27},
        {'category': 'Category B', 'value': 25},
        {'category': 'Category C', 'value': 18},
        {'category': 'Category D', 'value': 15},
        {'category': 'Category E', 'value': 10},
        {'category': 'Other', 'value': 5},
    ],
    innerRadius=0.6,
    width=600,
    height=400,
    title='Donut Chart'
)
render_pie_chart(options, "output/pie.png")

options = RadarChartOptions(
    data=[
        {'name': 'Sales', 'value': 70},
        {'name': 'Marketing', 'value': 60},
        {'name': 'Development', 'value': 80},
        {'name': 'Support', 'value': 40},
        {'name': 'Administration', 'value': 50},
    ],
    width=600,
    height=400,
    title='Performance Metrics'
)
render_radar_chart(options, "output/radar.png")

options = SankeyChartOptions(
    data=[
        {'source': 'Landing Page', 'target': 'Product Page', 'value': 50000},
        {'source': 'Product Page', 'target': 'Add to Cart', 'value': 35000},
        {'source': 'Add to Cart', 'target': 'Checkout', 'value': 25000},
        {'source': 'Checkout', 'target': 'Payment', 'value': 15000},
        {'source': 'Payment', 'target': 'Purchase Completed', 'value': 8000},
    ],
    width=800,
    height=600,
    title='User Flow'
)
render_sankey_chart(options, "output/sankey.png")

options = ScatterChartOptions(
    data=[
        {'x': 10, 'y': 15},
        {'x': 20, 'y': 25},
        {'x': 30, 'y': 35},
        {'x': 40, 'y': 45},
        {'x': 50, 'y': 55},
    ],
    width=600,
    height=400,
    title='Scatter Plot',
    axisXTitle='X Value',
    axisYTitle='Y Value'
)
render_scatter_chart(options, "output/scatter.png")

options = TreemapChartOptions(
    data=[
        {
            "name": "Root",
            "value": 100,
            "children": [
                {"name": "Category A", "value": 50},
                {"name": "Category B", "value": 30},
                {"name": "Category C", "value": 20},
            ],
        }
    ],
    width=600,
    height=400,
    title='Treemap'
)
render_treemap_chart(options, "output/treemap.png")

options = VennChartOptions(
    data=[
        {'label': 'A', 'value': 10, 'sets': ['A']},
        {'label': 'B', 'value': 20, 'sets': ['B']},
        {'label': 'C', 'value': 30, 'sets': ['C']},
        {'label': 'AB', 'value': 5, 'sets': ['A', 'B']},
    ],
    width=600,
    height=400,
    title='Venn Diagram'
)
render_venn_chart(options, "output/venn.png")

options = ViolinPlotOptions(
    data=[
        {'category': 'Group A', 'value': 10},
        {'category': 'Group A', 'value': 20},
        {'category': 'Group A', 'value': 30},
        {'category': 'Group B', 'value': 25},
        {'category': 'Group B', 'value': 35},
        {'category': 'Group B', 'value': 45},
    ],
    width=600,
    height=400,
    title='Violin Plot',
    axisXTitle='Group',
    axisYTitle='Value'
)
render_violin_chart(options, "output/violin.png")

options = WordCloudChartOptions(
    data=[
        {'value': 4.272, 'text': 'G2Plot'},
        {'value': 3.5, 'text': 'AntV'},
        {'value': 2.5, 'text': 'F2'},
        {'value': 2.2, 'text': 'Chart'},
        {'value': 2.0, 'text': 'Graphics'},
        {'value': 1.8, 'text': 'Plot'},
        {'value': 1.5, 'text': 'Visualization'},
    ],
    width=600,
    height=400,
    title='Word Cloud'
)
render_word_cloud_chart(options, "output/word-cloud.png")
