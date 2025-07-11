#!/usr/bin/env node
import { render } from '@antv/gpt-vis-ssr';

async function main() {
  // Get options from command line argument
  const optionsArg = process.argv[2];

  if (!optionsArg) {
    console.error('Usage: gpt-vis-cli <json_options>');
    process.exit(1);
  }

  let options;
  try {
    options = JSON.parse(optionsArg);
  } catch (error) {
    console.error('Error parsing JSON options:', error.message);
    process.exit(1);
  }

  try {
    const vis = await render(options);
    const buffer = vis.toBuffer();
    process.stdout.write(buffer, () => {
      // console.log('Visualization rendered successfully. Output written to stdout.');
      process.exit(0);
    });
  } catch (error) {
    console.error('Error rendering visualization:', error.message);
    process.exit(1);
  }
}

main();
