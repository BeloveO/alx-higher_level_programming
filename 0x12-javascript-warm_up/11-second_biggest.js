#!/usr/bin/node
const len = process.argv.length;
const nums = process.argv.slice(2).map(function (j) {
  return parseInt(j);
});
const max = Math.max.apply(Math, nums);
const min = Math.min.apply(Math, nums);

if (len > 3) {
  let i = 0;
  let j = 0;
  let secBig = min;

  for (; i < len; i++) {
    j = nums[i];

    if (j > secBig && j < max) {
      secBig = j;
    }
  }

  console.log(secBig);
} else {
  console.log(0);
}
