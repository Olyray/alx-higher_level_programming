#!/usr/bin/node
const fs = require('fs');

// Check if the file path is provided as an argument

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
