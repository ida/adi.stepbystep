function toggleTotalsOnly() {
  $('li:nth-child(3)').each(function() {
    var li = $(this)
    var text = li.text()
    if(text != 'Total:' && text != 'Totals:' && text != 'Actor') {
      li.parent().toggle()
    }
  });
}
(function($) { $(document).ready(function() {
  $('.toggleTotalsOnly').click(function() {
    toggleTotalsOnly()
  });
}); })(jQuery);
