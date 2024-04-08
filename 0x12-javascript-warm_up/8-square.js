#!/usr/bin/node

const squareSize = process.argv[2];
const input = parseInt(squareSize, 10);
const charPrint = 'X';
let countRow = 0;
let countX = 0;

if (isNaN(input)) {
	console.log('Missing size');
} else {
  for (let row = 0; row < input; row++) {
    let line = '';
    for (let col = 0; col < input; col++) {
      line += charPrint;
    }
    console.log(line);
  }
}
