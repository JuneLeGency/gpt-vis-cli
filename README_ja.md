# gpt-vis

[gpt-vis-cli](https://github.com/connect-a-sketch/gpt-vis-cli) の Python ラッパーで、プログラムおよびコマンドラインからチャートを生成できます。

## インストール

pip を使用してパッケージをインストールします:

```bash
pip install gpt-vis
```

または、リポジトリをクローンした場合は、Poetry を使用して編集可能モードでインストールできます:

```bash
poetry install
```

## 使用方法

### Python ライブラリとして

`gpt-vis` を使用して、Python アプリケーション内でプログラム的にチャートを生成できます。

```python
from gpt_vis.charts import render_bar_chart, BarChartOptions, BarChartData

# 棒グラフのオプションを定義します
bar_chart_options = BarChartOptions(
    data=[
        BarChartData(category="A", value=10),
        BarChartData(category="B", value=20),
        BarChartData(category="C", value=15),
    ],
    title="サンプル棒グラフ",
    axisXTitle="カテゴリ",
    axisYTitle="値",
)

# 棒グラフをレンダリングしてファイルに保存します
render_bar_chart(options=bar_chart_options, output_path="bar_chart.png")
```

### コマンドラインツールとして

`gpt-vis` は、簡単なチャート生成のためのコマンドラインインターフェイスも提供しています。

```bash
gpt-vis '''{"type": "bar", "data": [{"category": "A", "value": 10}, {"category": "B", "value": 20}], "title": "マイチャート"}''' output.png
```

## 利用可能なチャート

`gpt-vis` は、さまざまなチャートタイプをサポートしています:

- エリア
- 棒
- 箱ひげ図
- 縦棒
- 行政区分図
- 2軸
- 特性要因図
- フロー図
- じょうご
- ヒストグラム
- 折れ線
- リキッド
- マインドマップ
- ネットワーク図
- 組織図
- 経路図
- 円
- レーダー
- サンキー
- 散布図
- ツリーマップ
- ベン図
- バイオリン図
- ワードクラウド

各チャートタイプの詳細なオプションについては、`gpt_vis/charts.py` ファイルを参照してください。

## 開発

テストを実行するには、次のコマンドを実行します:

```bash
poetry run pytest
```

デモを実行するには、`output` ディレクトリにさまざまなチャート画像を生成します:

```bash
poetry run python run.py
```
