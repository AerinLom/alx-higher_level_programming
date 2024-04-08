#!/usr/bin/node

const arg1 = process.argv[2];
const isInt = parseInt(arg1, 10);

if (!isInt) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg1);
}
