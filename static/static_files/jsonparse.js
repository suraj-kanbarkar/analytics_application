//
//function jsonFunction() {
//var myArray = [
//  {
//    "display": "JavaScript Tutorial",
//    "url": "http://127.0.0.1:8000/callentry/"
//  },
//  {
//    "display": "HTML Tutorial",
//    "url": "https://www.w3schools.com/html/default.asp"
//  },
//  {
//    "display": "CSS Tutorial",
//    "url": "https://www.w3schools.com/css/default.asp"
//  }
//];
//  var out = "";
//  var i;
//  for(i = 0; i < myArray.length; i++) {
//    out += '<a href="' + myArray[i].url + '">' +
//    myArray[i].display + '</a><br>';
//  }
//  console.log(out)
//  document.getElementById("id01").innerHTML = out;
//}
//
//$(document).ready(function(){
//  $("#b").click(function(){
//    $.get("http://127.0.0.1:8000/callentry/", function(data, status){
//      alert("data: " + data, "\nStatus: " + status);
//      console.log(data)
//    });
//  });
//});