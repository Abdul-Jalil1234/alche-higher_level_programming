#!/usr/bin/node
const request = require('request');
const url = process.argv;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    if (film.characters.includes('https://alx-tools.com')) {
      count++;
    }
  }
  console.log(count);
});
