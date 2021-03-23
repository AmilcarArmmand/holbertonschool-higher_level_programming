#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer:
*/
'use strict';
const argList = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const arg in argList) {
  console.log(argList[arg]);
}
