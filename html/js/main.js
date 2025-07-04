document.writeln("<h1> Hello World ! </h1>");

// Comment line

// userName = prompt("Enter Your Name:\n"); // def type is string

// document.writeln("<h1> Hello "+userName+" </h1>");

//window.alert("Hello "+ userName);

//ans = window.confirm("Are You Sure?");

// document.writeln("User select : " + ans);

// operators

// Assignment Operator
// =, +=, -=, *=, /=, %=

// Arithmetic Operator
// +, -, *, /, % , ++, -- , **
// +=, -=, *=, /=, %=

// Comparison Operator
// ==, ===, !=, !==, >, <, >=, <=

// Logical Operator 
// &&, ||, !

// Ternary Operator
// ? :





// spread operator
// ...


// concatenation 

fname = "Anish"
lname = "Sony"

fullName = fname + " " + lname;

// unary operator

let a =+ "10";
let b =- "10";
let c =- "-10";
console.log(c);

// variables 

//var i = 10; // function scope, out of function
let j = 20; // block scope , we write code inside curly braces {}
const PI = 3.14; // constant

// var i = 20;
function sum(){
    let i = 10;
    console.log(i);
}

sum();

console.log(PI);

// local and global scope

var i = 10; // global scope

function sum(){
    console.log(i); // undefined, because we declare i inside function
    var i = 20; // local scope
}

function sum2(){
    let i =30;
    console.log(i); // 30
}

console.log(i); // 10 

// Data Types 

// String 
// Number 
// Boolean
// BigInt 
// Undefined 
// Null
// Symbol
// Object

// Type Casting

// String to Number

let x  = "10";

x = Number(x); // 10 Number

x = parseInt(x); // 10 Integer

x = 10;

x = x.toString(); // "10"
x = String(x); // "10"



// Date()

let date = new Date();

console.log(date.getMonth());// getDate(), getFullYear(),
//  getMonth(), getHours(), getMinutes(), getSeconds(), getMilliseconds()

// Built in functions

// String
// Striing is immutable - we cont't change the string
// String is a object
// String is a sequence of characters
 
let str = "Anish"; // literal
let str2 = new String("Anish"); // object

str.length; // 5
str.toUpperCase(); // ANISH
str.toLowerCase(); // anish
str.charAt(0); // A

document.writeln(str.slice(0,3)); //ani

str.split(""); // ["A","n","i","s","h"]

str.indexOf("i"); //2
str.replace("A","B"); // Bnish
str.replace("Anish","Sony"); // Sony
str.startsWith("A"); // true
str.endsWith("h"); // true
str.lastIndexOf("0"); // -1
str.includes("A"); // true
console.log(str.search("i"));

console.log(str[4]);

// "Anish" -> hsinA
// "Hello World" -> "dlroW olleH"
// "Hello World" -> "olleH dlroW" 
