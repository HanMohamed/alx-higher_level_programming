#!/usr/bin/node

/* a script that concats 2 files. */

const fs = require('fs');
const { EOL } = require('os');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

let content;

fs.open(fileC, 'w+', function (err) {
  if (err) throw err;
});

content = fs.readFileSync(fileA, 'utf8');
fs.appendFile(fileC, content, function (err) {
  if (err) throw err;
});
// fs.appendFile(fileC, EOL, function (err) {
//   if (err) throw err;
// });

content = fs.readFileSync(fileB, 'utf8');
fs.appendFile(fileC, content, function (err) {
  if (err) throw err;
});
// fs.appendFile(fileC, EOL, function (err) {
//   if (err) throw err;
// });
