#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let countOccur = 0;
  for (const value of list) {
    if (value === searchElement) {
      countOccur++;
    }
  }
  return countOccur;
};
