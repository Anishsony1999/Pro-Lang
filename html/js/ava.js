
// window.alert("Hello World")


// userInput = window.confirm("Are You Sure? ") // confirm function return boolean value(ture or false)

// alert(userInput)

// user_name = prompt("Enter Your Name");

// ans = confirm("Aru Your Sure To Display Your Name? ");

// if (ans ==true) document.writeln("<h1> Welcome "+ user_name +"</h1>")
// else document.writeln("<h1> Welcome Guest </h1>")

// condition ? true : false;
// ans ? document.writeln("<h1> Welcome "+ user_name +"</h1>") : document.writeln("<h1> Welcome Guest </h1>");

// spread operator
// ...

let arr1 = [1,2,3,4]
let arr2 = [5,6,...arr1,7,8]
console.log(arr2)

// str concation

fname = "avanthika"
lname = "R"
console.log( fname + " " + lname)
console.log(`${fname} ${lname}`)

// unary operator

let a =+ "10"; 
let b =- "10";
let c =- "-10";
console.log(c);

console.log(a)
console.log(typeof(a))

// variable declaration 

var i = 10;
let j = 20;
const k = 30;

var i = 100; // global scope

function sum(){
    let j = 200;
    let i = 200; //  local scope
    console.log("Value of i is : " + i);
}
sum();

console.log("Value of i is : "+i);

// Data types

// number 
// string
// boolean
// null
// undefined
// object

i = 10;
console.log(typeof(i)); // number

i = "10";
console.log(typeof(i)); // string

i = true;
console.log(typeof(i)); // boolean

i = null;
console.log(typeof(i)); // object

i = undefined;
console.log(typeof(i)); // undefined

i = {
    name : "avanthika",
};
console.log(typeof(i)); // object


// String

// String is immutable
// String is Object
// String is a sequence of characters

name = "Avanthika";
console.log(name[6]) // A

// string methods

names = "anish"
console.log(name);
console.log(name.length); // 10
console.log(name.toUpperCase());
console.log(name.toLowerCase());
console.log(name.trim()); // remove white space 
// console.log(name.capitalize())
console.log(name.charAt(0)); // A
console.log(name.replace("A","B")); // Bvanthika
console.log(name.replace("Avanthika","Sony")); // Sony
console.log(name.startsWith("A")); // false
console.log(name.endsWith("a")); // false

console.log(name.split("t"))
console.log(name.indexOf("i"))

console.log(Math.PI)
Math.min(12,4,5,6)
Math.max(23,5);
Math.round(4.4) // 4
Math.floor(4.9) // 4
Math.ceil(4.1) // 5
Math.abs(-4) // 4

console.log(Math.round(Math.random() * 10))

date =  new Date(); // creating new date object
console.log(date);
console.log(date.getTime())
console.log(date.getFullYear())
console.log(date.getMonth())
console.log(date.getDate())
console.log(date.getHours())
console.log(date.getMinutes())
console.log(date.getSeconds())
console.log(date.getMilliseconds())

let timeFormation = {
    year : "numeric",
    month : "long",
    day : "numeric",
}

console.log(date.toLocaleString("en-GB",timeFormation))

// array 

arr = []
arr2 = new Array();

x = [1,"Anish",true,10.0]
 
console.log(x[1])

// two dimensional array

x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

console.log(x[1][1]);

// JSON - JavaScript Object Notation

x = ["Anish",24,"Tvm"]

user ={
    'name' : 'Anish',
    'age' : 24,
    'city' : 'Tvm'
}

console.log(user['name'])
console.log(user.name)
console.log(x[0])

JSON.stringify(user) // convert object to string
//JSON.parse(user) // convert string to object

// Array Handling Methods

names = ["Anish","Avanthika"]

// push()
names.push("Sony") // adding element at the end
names.unshift("Ava") // adding element at the beginning

console.log(names)

names.pop() // removing element from the end
console.log(names)

names.shift() // removing element from the beginning
console.log(names)

// names.splice(1,1) // removing element from the index 1

console.log(names)

names.reverse() 

console.log(names)

names.sort()

console.log(names)

// toSrting()
// Array to String

console.log(names.toString())


