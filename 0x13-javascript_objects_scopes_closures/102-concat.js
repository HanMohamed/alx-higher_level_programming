#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// fs.writeFile(fileC, '');
let content;

content = fs.readFileSync(fileA, 'utf8');
content += '\n';
content += fs.readFileSync(fileB, 'utf8');

fs.writeFile(fileC, content, function (err) {
  if (err) throw err;
});
