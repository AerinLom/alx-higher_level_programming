#!/usr/bin/node

const argExists = process.argv[2];

if (!argExists) {
  console.log('No argument');
} else {
  console.log(argExists);
}
