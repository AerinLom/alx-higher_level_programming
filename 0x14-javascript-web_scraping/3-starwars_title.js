#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const urlRequest = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(urlRequest, { json: true }, (err, response, body) => {
  if (err) {
    console.error(`Error: ${err.message}`);
    return;
  }
  console.log(body.title);
});
