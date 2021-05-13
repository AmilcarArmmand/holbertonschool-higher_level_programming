/* JavaScript script that displays the value of hello in the HTML tag DIV#hello */
/* from URL: https://fourtonfish.com/hellosalut/?lang=fr */
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (body) {
  $('DIV#hello').text(body.hello);
});
