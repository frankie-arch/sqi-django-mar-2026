console.log("Hello world");
document.addEventListener("DOMContentLoaded", function(){

const bar = document.getElementById("announcement-bar");
const closeBtn = document.getElementById("close-announcement");

setTimeout(function(){
    bar.classList.add("show");
},2000);

closeBtn.addEventListener("click", function(){
    bar.classList.remove("show");
});

});