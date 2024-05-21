#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  const results = JSON.parse(body).results;
  const count = results.reduce((acc, movie) => {
    return movie.characters.some(character => character.endsWith('/18/')) ? acc + 1 : acc;
  }, 0);
  console.log(count);
});
