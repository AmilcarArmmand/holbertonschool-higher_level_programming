#!/usr/bin/node
/* a script that searches the second biggest integer in the list of arguments */
'use strict';
const numbers = process.argv;
if (process.argv.length < 4) {
  console.log(0);
} else {
  numbers.sort(function (a, b) {
    return b - a;
  });
  console.log(numbers[3]);
}
