#!/usr/bin/node

const arr = require('./100-data')
console.log(arr);
console.log(arr.map((num, index) => num * index));
