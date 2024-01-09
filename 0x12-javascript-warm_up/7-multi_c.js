#!/usr/bin/node

const multiLang = 'C is fun';
const times = process.argv[2];

if (!Number.isInteger(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log(multiLang);
  }
}
