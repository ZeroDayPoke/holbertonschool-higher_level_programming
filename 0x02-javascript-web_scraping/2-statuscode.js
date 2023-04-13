#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('I can has URL plz');
} else {
  const url = process.argv[2];
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` :( An error occurred while making the GET request: ${error}`);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
}
