#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Check if the URL and file path are provided as arguments
if (process.argv.length < 4) {
  console.error('Error: Please provide the URL and file path as arguments');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`The contents of ${url} have been saved to ${filePath}`);
  });
});
