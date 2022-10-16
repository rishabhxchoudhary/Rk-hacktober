

var rockCounter=document.getElementById('rock');
var paperCounter=document.getElementById('paper');
var scissorsCounter=document.getElementById('scissors');

var counter=Number(document.getElementById('count').innerText);
console.log(counter);

var greet=document.getElementById('result');
// greet.innerText='you have won';


function rockClick(){
    console.log('rock');
    var versus=rand(arr);

    if(versus=='paper'){
        console.log('lost');
        counter--;
        console.log(counter);
        document.getElementById('count').innerText=counter;
        greet.innerText=`AI chose ${versus}. You Lost`;
    }

    else if(versus=='scissors'){
        console.log('won');
        counter++;
        console.log(counter);
        document.getElementById('count').innerText=counter;
        greet.innerText=`AI chose ${versus}. You won`;

    }

    else{
        console.log('tie');
        greet.innerText=`AI chose ${versus}. It's tie`;
    }
}

function paperClick(){
    console.log('paper');
    var versus=rand(arr);

    if(versus=='scissors'){
        console.log('lost');
        counter--;
        console.log(counter);
        document.getElementById('count').innerText=counter;
        greet.innerText=`AI chose ${versus}. You Lost`;
    }

    else if(versus=='rock'){
        console.log('won');
        counter++;
        console.log(counter);
        document.getElementById('count').innerText=counter;
        greet.innerText=`AI chose ${versus}. You won`;
    }

    else{
        console.log('tie');
        greet.innerText=`AI chose ${versus}. It's tie`;
    }
}

function scissorsClick(){
    console.log('scissors');
    var versus=rand(arr);

    if(versus=='rock'){
        console.log('lost');
        counter--;
        console.log(counter);
        document.getElementById('count').innerText=counter;
        greet.innerText=`AI chose ${versus}. You Lost`;
    }

    else if(versus=='paper'){
        console.log('won');
        counter++;
        console.log(counter);
        document.getElementById('count').innerText=counter;
        greet.innerText=`AI chose ${versus}. You won`;
    }

    else{
        console.log('tie');
        greet.innerText=`AI chose ${versus}. It's tie`;
    }
}

function clearClick(){
    console.log('clear');
    document.getElementById('count').innerText=0;
    greet.innerText='';
}

let arr=['rock','paper','scissors'];

function rand(arr){
    let index=Math.floor(Math.random()*3);

    console.log('comp');
    console.log(arr[index]);
    return arr[index];
}



// rand(arr);


