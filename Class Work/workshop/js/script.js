// var a=10;
// let b=10; //can use var or let
// var c;
// // const d=20;
// c=a+b;
// console.log(c);

function add(){
    var a=document.getElementById("number1").value;
    var b=document.getElementById("number2").value;

    var c=parseInt(a)+parseInt(b);
    document.getElementById("answer").value=c;

    // console.log(a);
    // console.log(b);
}