#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('arg error');
} else {
  const filePath = process.argv[2];
  const contentToWrite = process.argv[3];

  fs.writeFile(filePath, contentToWrite, 'utf8', (error) => {
    if (error) {
      console.error(` :( An error occurred while writing to the file: ${error}`);
    }
  });
}
