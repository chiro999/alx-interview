#!/usr/bin/node
// This line specifies the interpreter for the script.

const request = require('request');
// This line imports the 'request' module, which allows making HTTP requests.

const API_URL = 'https://swapi-api.hbtn.io/api';
// This line defines the base URL for the Star Wars API that the script will interact with.

if (process.argv.length > 2) {
  // This line checks if command-line arguments have been provided when running the script.

  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // This line makes an HTTP GET request to fetch information about a specific film from the Star Wars API.

    if (err) {
      console.log(err);
      // This line logs any errors that occur during the HTTP request.
    }

    const charactersURL = JSON.parse(body).characters;
    // This line parses the JSON response body and extracts the URLs of the characters appearing in the film.

    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // This line maps over the array of character URLs and creates a Promise for each character.

        request(url, (promiseErr, __, charactersReqBody) => {
          // This line makes an HTTP request to fetch the character data.

          if (promiseErr) {
            reject(promiseErr);
            // This line rejects the Promise if an error occurs during the HTTP request.
          }

          resolve(JSON.parse(charactersReqBody).name);
          // This line resolves the Promise with the character's name extracted from the response body.
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
    // This line waits for all character name requests to complete, joins the names with newline characters, and logs the result.
  });
}
