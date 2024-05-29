#!/usr/bin/node

// This sctipt gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
