#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie in the same order in /films/ */
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const x of JSON.parse(body).characters) {
    request(x, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
