function loadLink(link, loadLinkClass) {
  var href = link.attr('href')
  var anchorId = ''
  var loadContainer = null
  var loadedEle = null
  if(href.indexOf('#') != -1) {
    href = href.split('#')
    anchorId = href[1]
    href = href[0]
  }
  // If we have a link with class showText, insert after step-title:
  if( link.hasClass('showText') ) {
    // Create wrapper to load dest into:
    link.parent().append('<div class="loadWrapper"></div>')
    // Grab the newly created wrapper:
    loadContainer = link.find('~ div.loadWrapper')
  }
  // If we have a link with class showChildren, prepend to parent:
  else {
    loadContainer = $('<div class="loadWrapper"></div>')
                    .insertAfter( link.parent() )
  }
  // Load destination into wrapper:
  loadContainer.load(href + ' #' + anchorId, function() {
    // Fetch loaded content:
    loadedEle = loadContainer.find('#' + anchorId)
    // Now the wrapper has become superfluous, remove it:
    loadedEle.unwrap()
    // Apply click-listener to the new loaded links:
    onLoadLinkClick(loadedEle, loadLinkClass, anchorId)
    // Switch button for show/hide children-button:
    toggleChildrenButtons(link)
  });
}
function onLoadLinkClick(container, loadLinkClass) {
  // On click, check if content is already loaded,
  // if so, switch its visibility, if not, load content intially.
  container.find('.' + loadLinkClass).click(function(eve) {
    eve.preventDefault()
    var link = $(eve.target)
    var anchorId = link.attr('href').split('#')[1]
    // if #text, we need this:
    var content_container = link.parent()
    // else for #children, we need this:
    if(anchorId == 'children') {
      content_container = content_container.parent()
    }
    var content = $(content_container.find('#' + anchorId)[0]) // only 1st
    // Content has not been loaded yet, load it:
    if(content.length < 1) {
      loadLink(link, loadLinkClass, anchorId)
    }
    // Otherwise only toggle visibility:
    else {
      content.toggle()
      toggleChildrenButtons(link)
    }
  });
}
function toggleChildrenButtons(link) {
// TODO improve: Do not merely switch class-name,
// but really check, if content is visible or not,
// because beleaving is good, yet proving is better.
  if(link.hasClass('showChildren')) {
    link.removeClass('showChildren'); link.addClass('hideChildren')
  }
  else if(link.hasClass('hideChildren')) {
    link.removeClass('hideChildren'); link.addClass('showChildren')
  }
  else if(link.hasClass('showText')) {
    link.removeClass('showText'); link.addClass('hideText')
  }
  else if(link.hasClass('hideText')) {
    link.removeClass('hideText'); link.addClass('showText')
  }
}
function onSpacebarPress(container) {
  container.keypress(function(eve) { // a key is pressed
console.log(eve.charCode)
    if(eve.charCode == '32') { // it's the spacebar
      eve.target.click() // simulate click on focused/active-ele
    }
  });
}
function applyInitialEventListeners(container, loadLinkClass) {
  onLoadLinkClick(container, loadLinkClass)
  onSpacebarPress(container)
}
function showOnlyTotals(container) {
  $('li:nth-child(3)').css('border','1px solid red')
}
(function($) { $(document).ready(function() {
  var container  = $(document.body)
  var loadLinkClass = 'loadLink'
  applyInitialEventListeners(container, loadLinkClass)


  // DEV: put this in an own script and only load in context:
  if($('.template-step_activities').length > 0) {
    showOnlyTotals(container)
  }




  // DEV: disable some links from tabflow, provide an ui-config later:
  $('.stepsHead a').attr('tabindex', '-1')
}); })(jQuery);
