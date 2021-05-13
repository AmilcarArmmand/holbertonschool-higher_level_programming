/* JavaScript script that fetches and prints how to say “Hello” depending on the language */
const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
window.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.get(url + language, function (body) {
      $('DIV#hello').text(body.hello);
    });
  });
});
