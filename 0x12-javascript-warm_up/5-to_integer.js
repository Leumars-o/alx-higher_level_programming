#!/usr/bin/node
const { argv } = require('node:process');
const integer = parseInt(argv[2]);
if (integer) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
