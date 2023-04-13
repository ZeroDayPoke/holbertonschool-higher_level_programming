#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('we really gotta work on your argument passing...');
} else {
  const url = process.argv[2];
  const filePath = process.argv[3];

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` :( An error occurred while making the GET request: ${error}`);
      return;
    }

    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(` :( An error occurred while writing to the file: ${error}`);
      }
    });
  });
}
