#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  const completedTasks = body.reduce((users, task) => {
    if (task.completed) {
      users[task.userId] = (users[task.userId] || 0) + 1;
    }
    return users;
  }, {});

  console.log(completedTasks);
});
