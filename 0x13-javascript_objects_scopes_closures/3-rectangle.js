#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      } 
    }
    Print () {
        const width = parseInt(w);
        const height = parseInt(h);
        if (width) {
            for (let i = 0; i < width; ++i) {
                let j = 0;
                
                for (; j < height; ++j) {
                    process.stdout.write('X');
                }
                if (j === height) {
                    console.log('');
                }
            }
            if (i === width) {
                console.log('');
            }
        } 
    }
  }
