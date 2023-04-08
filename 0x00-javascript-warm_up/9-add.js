#!/usr/bin/node
const process = require('process');

function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('NaN');
} else {
  const sum = add(arg1, arg2);
  console.log(sum);
}
