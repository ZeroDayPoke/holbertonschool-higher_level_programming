#!/usr/bin/node
const process = require('process');

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = parseInt(process.argv[2]);
const result = factorial(arg);

console.log(result);
