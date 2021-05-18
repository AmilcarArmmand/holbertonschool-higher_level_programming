/* JavaScript script that fetches and prints how to say “Hello” depending on the language */
function getLanguage (event) {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  const code = $('#language_code:text').val();
  $.getJSON(url + code, function (data) {
    $('#hello').text(data.hello);
  });
}
window.onload = function () {
  $('#btn_translate:button').click(getLanguage);
  $('#language_code').keypress(function (event) {
    const keyCode = (event.keyCode ? event.keyCode : event.which);
    if (keyCode === 13) {
      getLanguage();
    }
  });
};
