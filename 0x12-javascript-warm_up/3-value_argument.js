#!/usr/bin/node
/* a script that prints the first argument passed to it */
'use strict';
const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
