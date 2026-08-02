#!/usr/bin/node
const request = require('request');

const url = 'https://alx-tools.com' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
