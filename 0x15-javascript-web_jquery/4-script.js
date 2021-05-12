/* JavaScript script that toggles the class of the <header> element */
/* when the user clicks on the tag DIV#red_header */
$('DIV#toggle_header').click(function () {
  if ($('header').attr('class') === 'green') {
    $('header').attr('class', 'red');
  } else {
    $('header').attr('class', 'green');
  }
});
