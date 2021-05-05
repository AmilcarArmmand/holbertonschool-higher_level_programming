#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie in the same order at /films/ response */
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], async function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const x of JSON.parse(body).characters) {
    await new Promise(function (resolve, reject) {
      request(x, function (error, response, body) {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
