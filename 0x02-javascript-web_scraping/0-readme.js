#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Can has file doe? kthx');
} else {
  const filePath = process.argv[2];

  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      console.error(` :( An error occurred while reading the file: ${error}`);
      return;
    }
    console.log(data);
  });
}
