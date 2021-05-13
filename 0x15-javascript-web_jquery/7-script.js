/* JavaScript script that fetches the character name from URL */
/* https://swapi-api.hbtn.io/api/people/5/?format=json */
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (body) {
  $('DIV#character').text(body.name);
});
