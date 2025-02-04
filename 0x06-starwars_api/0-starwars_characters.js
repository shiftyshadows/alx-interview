#!/usr/bin/node
/**
 * Star Wars Movie Characters Script
 *
 * This script takes a movie ID as a positional argument and prints all
 * character names from the given Star Wars movie in the same order as in the
 * API.
 *
 * Usage:
 *    node starwars_characters.js <movie_id>
 *
 * Requirements:
 *    - request-promise (npm install request-promise)
 *
 * Example:
 *    node starwars_characters.js 3
 *    (Outputs all characters from "Return of the Jedi")
 */
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
