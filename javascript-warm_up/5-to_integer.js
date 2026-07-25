#!/usr/bin/node
const firstArg = process.argv;
const parsedNum = parseInt(firstArg, 10);

if (Number.isNaN(parsedNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsedNum);
}
