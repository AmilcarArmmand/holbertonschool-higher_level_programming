#!/usr/bin/node
/* a script that computes the number of tasks completed by user id */
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const results = JSON.parse(body);
    for (const i of results) {
      const uid = i.userId.toString();
      const task = i.completed;
      if (task) {
        completed[uid] = completed[uid] || 0;
        completed[uid] = completed[uid] + 1;
      }
    }
    console.log(completed);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
