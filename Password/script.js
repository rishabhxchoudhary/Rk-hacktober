const input = document.querySelector("input");

window.addEventListener('load',(e)=>{console.log(e)});

const img = document.querySelector("img");
let length = input.value.length;
input.addEventListener("input", (e) => {
  length = e.target.value.length;
  img.style.filter = `blur(${length}px)`;

  console.log(length);
});
