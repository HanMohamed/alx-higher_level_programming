#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let str;
      for (let i = 0; i < this.height; i++) {
        str = c;
        for (let j = 0; j < (this.width - 1); j++) {
          str += c;
        }
        console.log(str);
      }
    }
  }
}

module.exports = Square;
