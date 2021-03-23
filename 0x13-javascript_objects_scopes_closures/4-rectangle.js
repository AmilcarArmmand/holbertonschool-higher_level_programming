#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle
create instance called rotate() that exchanges width and height of rectangle
create instance called double() that multiples width and height of rectangle by 2
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width; // this.height = this.width ^ this.height;
    this.width = this.height; // this.width = this.height ^ this.width;
    this.height = temp; // this.heght = this.width ^ this.height;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
