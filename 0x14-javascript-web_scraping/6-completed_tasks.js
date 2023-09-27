#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (_err, _response, body) {
  if (_err) {
    console.log(_err);
  } else {
    const userscompleted = {};
    body = JSON.parse(body);
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;
      if (completed && !userscompleted[userId]) {
        userscompleted[userId] = 0;
      }
      if (completed) ++userscompleted[userId];
    }
    console.log(userscompleted);
  }
});
