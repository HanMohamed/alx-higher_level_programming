#!/usr/bin/node

const startArg = 2;

if (!process.argv[startArg]) {
  console.log('No argument');
} else {
  process.argv.forEach(val => {
    console.log(`${val}`);
  });
}
