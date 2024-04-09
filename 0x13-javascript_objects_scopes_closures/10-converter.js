#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    const convertedNum = number.toString(base);
    return convertedNum;
  };
};
