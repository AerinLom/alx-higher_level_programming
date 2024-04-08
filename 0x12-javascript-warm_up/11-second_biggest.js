#!/usr/bin/node

const intValues = process.argv.slice(2).map(Number);
const sortedList = intValues.sort((a, b) => b - a);

if (intValues.length <= 1) {
  console.log(0);
} else {
  console.log(sortedList[1]);
}
