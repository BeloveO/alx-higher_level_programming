const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  const result = data.results;
  for (let i = 0; i < result.length; i++) {
    $('UL#list_movies').append('<li>' + result[i].title + '</li>');
  }
});
