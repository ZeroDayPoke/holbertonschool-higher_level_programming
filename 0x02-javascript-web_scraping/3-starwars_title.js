#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
  console.error('use the force fool');
} else {
  const movieId = process.argv[2];
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(` :( An error occurred while making the GET request: ${error}`);
      return;
    }

    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    } else {
      console.error(` :( An error occurred while fetching the movie: ${response.statusCode}`);
    }
  });
}
