#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c !== 'C') {
      super.print();
    } else {
      let str;
      for (let i = 0; i < this.height; i++) {
        str = 'C';
        for (let j = 0; j < (this.width - 1); j++) {
          str += 'C';
        }
        console.log(str);
      }
    }
  }
}

module.exports = Square;
