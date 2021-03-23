#!/usr/bin/node
/* a function that returns the reversed version of a list */
exports.esrever = function (list) {
  const reversed = [];
  for (let i = 0; i < list.length; i++) {
    reversed.unshift(list[i]);
  }
  return reversed;
};
