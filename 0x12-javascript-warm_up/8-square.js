#!/usr/bin/node

const square = 'X';
const times = process.argv[2];
let squareLength = '';

if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    squareLength = '';
    for (let j = 0; j < times; j++) {
      squareLength += square;
    }
    console.log(squareLength);
  }
}
