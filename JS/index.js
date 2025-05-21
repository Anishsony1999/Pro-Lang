
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

num1 = prompt("Enter a number ");
num2 = prompt("Enter a number ");

console.log(num1 + num2); // string concatenation 2020
console.log(parseInt(num1) + parseInt(num2)); // parseInt() converts string to integer 20 + 20

