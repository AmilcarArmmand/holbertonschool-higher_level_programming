#!/usr/bin/node
/* using the Star Wars API https://swapi-api.hbtn.io/ prints the title of the */
/* Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    const appears = results.filter((x) => x.characters.filter((y) => y.match(/people\/18\//)).length !== 0);
    console.log(appears.length);
  }
});
