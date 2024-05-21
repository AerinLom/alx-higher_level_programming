#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const urlPath = process.argv[2];
const file = process.argv[3];

request(urlPath, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
