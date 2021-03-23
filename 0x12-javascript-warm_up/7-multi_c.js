#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer:
*/
'use strict';
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x && !isNaN(x); i++) {
    console.log('C is fun');
  }
}
