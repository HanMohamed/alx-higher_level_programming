#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let str;
    for (let i = 0; i < this.height; i++) {
      str = 'X';
      for (let j = 0; j < (this.width - 1); j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    const widthTemp = this.width;
    this.width = this.height;
    this.height = widthTemp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
