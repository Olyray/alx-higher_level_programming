#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write('C');
        }
        console.log();
      }
    }
  }
};
