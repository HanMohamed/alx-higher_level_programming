#!/usr/bin/node

const argLength = process.argv.length;

function secondBiggest () {
  let bigger, secondBigger, argvNumb, prev;
  bigger = parseInt(process.argv[2]);
  secondBigger = bigger;

  for (let i = 3; i < argLength; i++) {
    argvNumb = parseInt(process.argv[i]);
    bigger = argvNumb > bigger ? argvNumb : bigger;
    prev = parseInt(process.argv[i - 1]);

    if (secondBigger === bigger && argvNumb < secondBigger) {
      secondBigger = argvNumb;
    } else if (secondBigger < bigger && secondBigger < prev) {
      secondBigger = prev;
    }
  }
  console.log(secondBigger);
}

if (argLength < 4) {
  console.log(0);
} else {
  secondBiggest();
}
