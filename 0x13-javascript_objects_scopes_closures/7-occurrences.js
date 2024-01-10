#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numb = 0;
  list.forEach(element => {
    numb += element === searchElement ? 1 : 0;
  });
  return (numb);
};
