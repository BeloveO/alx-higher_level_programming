#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let ntimes = 0;

request(url, function (_err, _response, body) {
  body = JSON.parse(body).results;
  for (let i = 0; i < body.length; ++i) {
    const chars = body[i].chars;
    for (let j = 0; j < chars.length; ++j) {
      const char = chars[j];
      const charid = char.split('/')[5];
      if (charid === '18') {
        ntimes += 1;
      }
    }
  }
  console.log(ntimes);
});
