let menu_btn = document.querySelector(".burger_menu_wrapper");
let close_btn = document.querySelector(".close")
let mobileMenu =document.querySelector(".mobile_menu_wrapper")

menu_btn.addEventListener("click",handleOpenMenu)
close_btn.addEventListener("click", handleCloseMenu)

function handleOpenMenu(){
  mobileMenu.style.display="flex"
  console.log("hello");
  menu_btn.style.display="none"
}
function handleCloseMenu (){
  mobileMenu.style.animation= " slideInBack 0.5s forwards"
  menu_btn.style.display="flex"
  document.querySelector(".burger_menu_wrapper").style.display="flex"
  setTimeout(()=>{
    mobileMenu.style.display="none"
    mobileMenu.style.animation= " slideInRight 0.5s forwards"
  },500)
  
}