let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  let movies = data.results;
  for (let movie of movies) {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
  }
});
