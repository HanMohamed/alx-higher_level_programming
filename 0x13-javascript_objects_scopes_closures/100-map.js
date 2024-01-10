#!/usr/bin/node

const list = require('./100-data').list;

const newList = [];
let i = 0;

list.forEach(element => {
  newList[i] = i * element;
  i++;
});

console.log(list);
console.log(newList);
