/* JavaScript script that fetches and lists the title for all movies */
/* from URL: https://swapi-api.hbtn.io/api/films/?format=json */
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (body) {
  for (const film of body.results) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  }
});
