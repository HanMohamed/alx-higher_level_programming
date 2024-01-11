#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};
let value;

for (const key in dict) {
  value = dict[key];

  if (!sortedDict[value]) {
    sortedDict[value] = [];
  }
  sortedDict[value].push(key);
}

console.log(sortedDict);
