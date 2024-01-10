#!/usr/bin/node

let numPrint = 0;

exports.logMe = function (item) {
  console.log(numPrint + ': ' + item);
  numPrint++;
};
