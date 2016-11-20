//Pure JS code with jQuery implementation
   

document.addEventListener('DOMContentLoaded', function() {

  var Button = document.getElementById('pressme');
  var input1 = document.getElementById('sample1');
  var input2 = document.getElementById('sample2');

  Button.addEventListener('click', function() {
  	var val1 = input1.value.toUpperCase()
  	var val2 = input2.value
  	chrome.downloads.download({url: "http://localhost:5000/RoCal/api/v1/"+val1+"/"+val2}, function(id) {});
  });

  


}, false);
