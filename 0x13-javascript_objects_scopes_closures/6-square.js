#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const height = this.height;
    const width = this.width;
    const printChar = c || 'X';

    for (let heightX = 0; heightX < height; heightX++) {
      let row = '';
      for (let widthX = 0; widthX < width; widthX++) {
        row += printChar;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
