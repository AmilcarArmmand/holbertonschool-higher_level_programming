#!/usr/bin/node
/* a script that searches the second biggest integer in the list of arguments */
'use strict';
const x = process.argv.slice(2);
if (x.length < 2) {
  console.log(0);
} else {
  x.sort();
  x.reverse();
  console.log(x[1]);
}
