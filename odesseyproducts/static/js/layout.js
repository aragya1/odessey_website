function footmobiledropdown(name) {
  var id_name = "foot-mobile-dropdown-".concat(name);
  var element = document.getElementById(id_name);
  if (element.style.display === "block"){
    element.style.display = "none";
    
  } else {
    element.style.display = "block";
  }

}

function opensidenav() {
  document.getElementById("sidenav").style.width = "250px";
  document.getElementById("sidenav").style.paddingLeft = "40px";
}

function closesidenav() {
  document.getElementById("sidenav").style.width = "0px";
  document.getElementById("sidenav").style.paddingLeft = "0px";
}

