#!/usr/bin/node
// Fetches and prints the title of a Star Wars movie based on a given episode ID

const request = require('request');
const episodeId = process.argv[2];
const url = `https://alx-tools.com{episodeId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
