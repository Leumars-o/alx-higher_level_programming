#!/usr/bin/node

// import filesystem module
const fs = require('fs');

// write to the file
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
