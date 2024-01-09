#!/usr/bin/node

const argLength = process.argv.length;

function secondBiggest () {
  let bigger, secondBigger, curr;
  bigger = parseInt(process.argv[2]);
  secondBigger = bigger;

  for (let i = 3; i < argLength; i++) {
    curr = parseInt(process.argv[i]);
    secondBigger = curr > bigger ? bigger : secondBigger;
    bigger = curr > bigger ? curr : bigger;
  }
  console.log(secondBigger);
}

if (argLength < 4) {
  console.log(0);
} else {
  secondBiggest();
}
