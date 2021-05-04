#!/usr/bin/node
/* a script that gets the contents of a webpage and stores it in a file */
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body.toString(), 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
