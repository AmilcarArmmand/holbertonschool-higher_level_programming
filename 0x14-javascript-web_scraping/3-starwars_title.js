#!/usr/bin/node
/* using the Star Wars API https://swapi-api.hbtn.io/ prints the title of the */
/* Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const title = process.argv[2];

request(url + title, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
