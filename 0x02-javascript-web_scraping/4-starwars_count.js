#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('put URL into these paws');
} else {
  const apiUrl = process.argv[2];
  const characterId = 18;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(` :( An error occurred while making the GET request: ${error}`);
      return;
    }

    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let count = 0;

      films.forEach((film) => {
        if (film.characters.some((characterUrl) => characterUrl.includes(`/people/${characterId}/`))) {
          count += 1;
        }
      });

      console.log(count);
    } else {
      console.error(` :( An error occurred while fetching the films: ${response.statusCode}`);
    }
  });
}
