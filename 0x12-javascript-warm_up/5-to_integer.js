#!/usr/bin/node

const numb = process.argv[2];

if (!numb || isNaN(numb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numb);
}
