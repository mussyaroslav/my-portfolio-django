function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function myFunction__nav() {
    document.getElementById("myDropdown__nav").classList.toggle("show");
}

function myFunction__theme() {
    document.getElementById("myDropdown__theme").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches(['.dropbtn', '.arrow__down__lang'])) {

    const dropdowns = document.getElementsByClassName("dropdown-content");
    let i;
    for (i = 0; i < dropdowns.length; i++) {
      const openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }

  if (!event.target.matches('.drop__btn__nav')) {

    const dropdowns__nav = document.getElementsByClassName("dropdown-content__nav");
    let i;
    for (i = 0; i < dropdowns__nav.length; i++) {
      const openDropdown__nav = dropdowns__nav[i];
      if (openDropdown__nav.classList.contains('show')) {
        openDropdown__nav.classList.remove('show');
      }
    }
  }

  if (!event.target.matches(['.dropbtn__theme', '.arrow__down__theme'])) {

    const dropdowns__nav = document.getElementsByClassName("dropdown-content-theme");
    let i;
    for (i = 0; i < dropdowns__nav.length; i++) {
      const openDropdown__nav = dropdowns__nav[i];
      if (openDropdown__nav.classList.contains('show')) {
        openDropdown__nav.classList.remove('show');
      }
    }
  }
}