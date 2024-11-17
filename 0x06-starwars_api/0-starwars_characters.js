#!/usr/bin/node
/**
 * This script prints all characters of a Star Wars movie.
 * The first positional argument is the Movie ID (e.g., 3 = "Return of the Jedi").
 * One character name is displayed per line in the same order as the "characters" list
 * from the SWAPI /films/ endpoint.
 */

const request = require('request');

// Function to fetch and print movie characters
const getMovieCharacters = (movieId) => {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(filmUrl, (error, response, body) => {
    if (error) {
      console.error('Error: Unable to fetch movie data.', error.message);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: Movie not found. HTTP Status: ${response.statusCode}`);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters || [];

    if (characterUrls.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    // Fetch and print each character's name
    let completedRequests = 0;
    characterUrls.forEach((url) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error: Unable to fetch character data.', charError.message);
          return;
        }

        if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error(`Error: Failed to fetch character. HTTP Status: ${charResponse.statusCode}`);
        }

        completedRequests++;
        // Ensure all requests are completed before exiting
        if (completedRequests === characterUrls.length) {
          process.exit(0);
        }
      });
    });
  });
};

// Main script execution
const args = process.argv.slice(2);

if (args.length !== 1) {
  console.error('Usage: ./star_wars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = parseInt(args[0], 10);

if (isNaN(movieId)) {
  console.error('Error: Movie ID must be an integer.');
  process.exit(1);
}

getMovieCharacters(movieId);
