//Pure JS code with jQuery implementation
   

document.addEventListener('DOMContentLoaded', function() {

  var Button = document.getElementById('pressme');
  Button.addEventListener('click', function() {
  	chrome.downloads.download({url: "http://freetexthost.com/t56wafd4pu"}, function(id) {});
  });

  


}, false);
