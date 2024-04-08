#!/usr/bin/node

const printNum = process.argv[2];
const occur = parseInt(printNum, 10);
const phrase = 'C is fun';
let count = 1;

if (!occur) {
  console.log('Missing number of occurrences');
} else {
  while (count !== printNum) {
    console.log(phrase);
    count++;
  }
}
