#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];

  for (let j = list.length - 1, i = 0; j >= 0; j--, i++) {
    revList[i] = list[j];
  }
  return (revList);
};
