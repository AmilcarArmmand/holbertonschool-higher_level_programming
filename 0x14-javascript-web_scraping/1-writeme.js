#!/usr/bin/node
/* script that writes a string to a file */
const fs = require('fs');
const file = process.argv[2];
const contents = process.argv[3];

fs.writeFile(file, contents, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
