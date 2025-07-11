#!/usr/bin/node
const size = Number(process.argv[2]);

if (!Number.isInteger(size)) {
  console.log('Missing size');
} else {
  let row = 0;
  while (row < size) {
    let col = 0;
    let line = '';
    while (col < size) {
      line += 'X';
      col++;
    }
    console.log(line);
    row++;
  }
}

