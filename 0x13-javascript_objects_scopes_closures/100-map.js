#!/usr/bin/node
const array = require('./100-data').list;
const newArray = array.map((x, index) => x * index);
console.log(Array);
console.log(newArray);
