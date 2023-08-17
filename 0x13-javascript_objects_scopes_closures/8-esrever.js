#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  for (let i = list - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
