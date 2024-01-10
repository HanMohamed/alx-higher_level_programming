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
}

module.exports = Rectangle;
