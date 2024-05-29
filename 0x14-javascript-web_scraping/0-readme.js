#!/usr/bin/node

// import the fs module
const fs = require('fs');
// read the file
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
