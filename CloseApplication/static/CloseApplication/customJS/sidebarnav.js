$(document).ready(function() {
    getCurrentURL()
});


function getCurrentURL() {
    var pathName = window.location.pathname;
    var returnIndexOfFirstPath = pathName.indexOf("/", 1);
    var returnIndexOfSecondPath = pathName.indexOf("/", returnIndexOfFirstPath);
    var dataType = pathName.substr(returnIndexOfFirstPath + 1, returnIndexOfSecondPath - 1);
    console.log(dataType);
};