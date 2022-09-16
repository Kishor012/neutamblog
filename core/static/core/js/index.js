
const header_flex_box_man = document.querySelectorAll(".header-flex-box-man")[0].childNodes[1];
const header_flex = document.querySelectorAll(".header-flex-box-man")[0].childNodes[3];

header_flex_box_man.classList.add("media_set_margin");
header_flex.classList.add("media_set_margin");

console.log(header_flex_box_man);

const navSlide = () => {
const navBars = document.querySelector('.logo span');
const navLinks = document.querySelector('nav ul');     
        navBars.addEventListener('click', () => {
        navLinks.classList.toggle('nav-active');
});    
}

navSlide();