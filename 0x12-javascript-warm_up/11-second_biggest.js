#!/usr/bin/node

const argLength = process.argv.length;

function secondBiggest () {
  let bigger, secondBigger, curr;
  bigger = 0;
  secondBigger = bigger;

  for (let i = 2; i < argLength; i++) {
    curr = parseInt(process.argv[i]);

    if (curr > bigger) {
      secondBigger = bigger;
      bigger = curr;
    } else if (curr > secondBigger) {
      secondBigger = curr;
    }
  }
  console.log(secondBigger);
}

if (argLength < 4) {
  console.log(0);
} else {
  secondBiggest();
}
