#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
