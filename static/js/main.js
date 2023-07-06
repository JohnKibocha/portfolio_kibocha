function toggleNavbar() {
      let navbar = document.getElementById("myNavbar");
      if (navbar.className === "navbar") {
        navbar.className += " responsive";
      } else {
        navbar.className = "navbar";
      }
    }