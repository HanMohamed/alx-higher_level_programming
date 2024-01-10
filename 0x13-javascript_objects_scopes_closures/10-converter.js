#!/usr/bin/node

/*
 * convert base 10 to any otherbase:
 *    number.tostring(any base);
 * convert any otherbase t0 base 10:
 *    parseInt(number, its base);
 * convert any base1 to any base2:
 *    1- numberBase_10 = parseInt(number, base1);
 *    2- numberNewBase = numberBase_10.toString(base2);
 */

exports.converter = function (base) {
  return function (numb) {
    return (numb.toString(base));
  };
};
