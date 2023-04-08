#!/usr/bin/node
const process = require('process');

if (process.argv.length > 4) {
  console.log('bad uwuser!');
} else {
  const arg1 = process.argv[2];
  const arg2 = process.argv[3];
  console.log(`${arg1} is ${arg2}`);
}
