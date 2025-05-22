
// comment


// single line comment
/*
multi line comment
*/

// var name = prompt("Enter a number "); // String data type

x = 10 + 20;

var welcomeMessage = "Welcome " + name ; // String concatenation
console.log(welcomeMessage);


// var vs let
// var a = 10;
// let b = 20;
// const c = 30;

// var vs let 
// var is function scoped
// let is block scoped

//global scope and local scope

let a = 10; // global scope

function add(){
    let a = 20; // local scope
    let b = 30;

    console.log(a + b);
}

console.log(a); // 10
// console.log(b); // error

add();


// Data types

// 1. Number - integer, float, double, long
// 2. String - ""
// 3. Boolean - true(1), false(0)
// 4. Undefined 
// 5. Null - empty

// num1 = prompt("Enter a number ");
// num2 = prompt("Enter a number ");

// console.log(num1 + num2); // string concatenation 2020
// console.log(parseInt(num1) + parseInt(num2)); // parseInt() converts string to integer 20 + 20


var str = "100";

var num = Number(str); // 100 int

const date = new Date();

// console.log(date);

// boolean val

var ans = Number(true); // true 1 | false 0


var ans = true ;
var printing =  ans ? 1 : 0 


// String handling

let uName = "Anish";
alert(uName.length);

fname = "anish";
lname = "sony";

fullName = fname.concat(" ",lname);

alert(fullName)

str = "welcome to tvm";

welcome  = str.replace("tvm" , "SCOPE INDIA");

alert(welcome);

str = "   i am from tvm   ";

out1 = str.length;
alert("str real length : " + out1); // 19

out = str.trim();

alert("after trim : " +  out.length); // 13
alert(out)


str.toUpperCase() // change to upper case
str.toLowerCase() // change to lower case

// Math functions

x = 20.2

Math.round(x); // 20.2 -> 20
Math.floor(x); // 20.2 -> 20
Math.ceil(x); // 20.2 -> 21

Math.min(10,20); // 10
Math.max(10,20); // 20
Math.pow(5,2); // 5**2
Math.abs(-18); // 18
Math.sqrt(25); // 5


// Date and Time


// const date = new Date();

alert(date);


date.getDate(); // date
date.getDay();
date.getFullYear();
date.getSeconds();
date.getHours();
date.getTime();




