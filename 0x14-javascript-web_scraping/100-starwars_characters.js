#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/'.concat(process.argv[2]);

request(url, function (_err, _response, body) {
  const chars = JSON.parse(body).chars;
  for (let i = 0; i < chars.length; ++i) {
    request(chars[i], function (_cerr, _cresponse, cbody) {
      console.log(JSON.parse(cbody).name);
    });
  }
});
