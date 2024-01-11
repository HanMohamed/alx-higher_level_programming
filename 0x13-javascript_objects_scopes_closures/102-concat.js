#!/usr/bin/node

/* a script that concats 2 files. */

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

let content;

content = fs.readFileSync(fileA, 'utf8');
content += '\n';
content += fs.readFileSync(fileB, 'utf8');
// content += '\n';

fs.writeFile(fileC, content, function (err) {
  if (err) throw err;
});
