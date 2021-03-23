#!/usr/bin/node
/* Write a function that increments and calls a function */
this.addMeMaybe = function (number, theFunction) {
  if (this.myNum === undefined) {
    this.myNum = 1;
  }
  theFunction(this.myNum + number);
  this.myNum += 1;
};
