function myFunction() {
    var x = document.getElementById("side");
    if (x.className === "sidebar") {
      x.className += " responsive";
    } else {
      x.className = "sidebar";
    }
    
    var x = document.getElementById("Content");
    if (x.className === "content") {
      x.className += " add";
    } else {
      x.className = "content";
    }
  }