#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/'.concat(process.argv[2]);

request(url, function (_err, _response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
