#!/usr/bin/node

exports.esrever = function (list) {
  const countValues = list.length;
  const revList = [];

  for (let index = countValues - 1; index >= 0; index--) {
    revList.push(list[index]);
  }
  return revList;
};
