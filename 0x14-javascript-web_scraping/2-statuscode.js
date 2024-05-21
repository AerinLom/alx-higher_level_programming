#!/usr/bin/node

const request = require('request');

const urlRequest = process.argv[2];

request.get(urlRequest, (err, response) => {
  if (err) {
    console.error(`Error: ${err.message}`);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
