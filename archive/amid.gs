function myFunction() {
  
}

function getAltmetricsScore(AMID) {
  var options = {
    'muteHttpExceptions' : true
  };
  var response = UrlFetchApp.fetch('https://www.altmetric.com/details/' + AMID,options);
  htmltxt = response.getContentText();
  return +htmltxt.substring(htmltxt.indexOf("score=")+6,htmltxt.indexOf("&types="));  
}



function getAltmetricsScoreOld(AMurl) {
  var options = {
    'muteHttpExceptions' : true
  };
  var response = UrlFetchApp.fetch(AMurl,options);
  htmltxt = response.getContentText();
  Logger.log(+htmltxt.substring(htmltxt.indexOf("score=")+6,htmltxt.indexOf("&types=")));  
  return +htmltxt.substring(htmltxt.indexOf("score=")+6,htmltxt.indexOf("&types="));  
}
