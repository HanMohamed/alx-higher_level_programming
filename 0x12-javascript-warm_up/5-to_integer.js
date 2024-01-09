#!/usr/bin/node

const numb = process.argv[2];

if (!numb || !Number.isInteger(numb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numb);
}
