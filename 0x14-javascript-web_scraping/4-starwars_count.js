#!/usr/bin/node

// This script prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

let count = 0;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
