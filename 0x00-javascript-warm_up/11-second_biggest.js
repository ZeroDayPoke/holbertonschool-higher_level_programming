#!/usr/bin/node
const process = require('process');

function secondLargest (numbers) {
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const number of numbers) {
    if (number > largest) {
      secondLargest = largest;
      largest = number;
    } else if (number > secondLargest && number !== largest) {
      secondLargest = number;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2).map(arg => parseInt(arg));

if (args.length <= 1) {
  console.log(0);
} else {
  const result = secondLargest(args);
  console.log(result);
}
