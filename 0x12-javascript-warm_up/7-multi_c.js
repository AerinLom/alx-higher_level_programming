#!/usr/bin/node

const printNum = process.argv[2];
const occur = parseInt(printNum, 10);
const phrase = 'C is fun';
let count = 0;

if (isNaN(occur)) {
  console.log('Missing number of occurrences');
} else {
  while (count < occur) {
    console.log(phrase);
    count++;
  }
}
