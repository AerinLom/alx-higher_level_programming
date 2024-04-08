#!/usr/bin/node

const squareSize = process.argv[2];
const input = parseInt(squareSize, 10);
const charPrint = 'X';
let count = 0;

if (isNaN(input)) {
	console.log('Missing size');
} else {
  while (count < input) {
    console.log(charPrint.repeat(input));
    count++;
  }
}
