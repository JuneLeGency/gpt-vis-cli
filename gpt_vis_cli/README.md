# gpt-vis-cli

A command-line interface for rendering visualizations using `@antv/gpt-vis-ssr`.

## Description

This CLI tool provides a simple way to generate visualizations from the command line. It takes a JSON object as input, which specifies the type of chart and the data to be visualized. The tool then outputs the rendered visualization as a PNG image to standard output.

## Installation

Install the CLI globally using npm:

```bash
npm install -g gpt-vis-cli
```

## Usage

```bash
gpt-vis-cli '<json_options>' > output.png
```

### Arguments

-   `<json_options>`: A JSON string containing the options for rendering the visualization. The JSON object should have the following properties:
    -   `type`: The type of chart to generate (e.g., "line", "pie", "bar").
    -   `data`: An array of data objects to be visualized in the chart.

## Example

Here is an example of how to generate a line chart:

```bash
gpt-vis-cli '{"type":"line","data":[{"x":"Monday","y":3000},{"x":"Tuesday","y":3200},{"x":"Wednesday","y":2800},{"x":"Thursday","y":4000},{"x":"Friday","y":3500},{"x":"Saturday","y":3800},{"x":"Sunday","y":4200}]}' > line_chart.png
```

This command will generate a line chart and save it as `line_chart.png`.
