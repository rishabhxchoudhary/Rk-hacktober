// var n=document.getElementById('cookie');
var no=document.getElementById('cookie2');
var coun=document.getElementById('count');

no.addEventListener('click',function(){
    console.log('click');
    coun.innerHTML++;

});



// const url = new Audio("Elements/sound-onclick/click.mp3");

function playAudio(url) {
    new Audio(url).play();
  }





