#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && Number.isInteger(w)) && (h > 0 && Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const height = this.height;
    const width = this.width;

    for (let heightX = 0; heightX < height; heightX++) {
      let row = '';
      for (let widthX = 0; widthX < width; widthX++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
