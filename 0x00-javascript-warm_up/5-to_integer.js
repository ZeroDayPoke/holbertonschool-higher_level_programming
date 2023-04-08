#!/usr/bin/node
const process = require('process');

if (process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  const arg = process.argv[2];
  const integerArg = parseInt(arg);

  if (isNaN(integerArg)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${integerArg}`);
  }
}
