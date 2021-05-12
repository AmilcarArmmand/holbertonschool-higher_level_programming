/* JavaScript script that adds a <li> element to a list on click of the tag DIV#add_item */
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
