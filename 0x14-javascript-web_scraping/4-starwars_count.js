#!/usr/bin/node
const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Error: Please provide the API URL as an argument');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
  console.log(count);
});
