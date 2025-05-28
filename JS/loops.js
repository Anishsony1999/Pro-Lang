// what is loops?
// loops are used to repeat a block of code multiple times.
// there are two types of loops in javascript.
// 1. for loop
   // for in loop
   // for each loop
   // for of loop
// 2. while loop
    // do while loop


// document.writeln("hello world" + "<br>");
// for loop

// for (initialization; condition; increment/decrement) {}

for (let i = 1; i <= 100 ; i++){
    // document.writeln(i + ", hello world" + "<br>");
}


// while loop

// while (condition) {}

let i = 1;
while (i <= 10) {
    // document.writeln(i + ", hello world" + "<br>");
    i++;
}

// do while loop

// do {} while (condition);

let j = 1;
do {
    // document.writeln(j + ", hello world" + "<br>");
    j++;
} while (j <= 10);


// Task:
// 1. print all the even numbers from 1 to 100 using for loop
// 2. palindrome : amma , malayalam 


// 28 - 05 - 2025

// dedicated arrays / Object loops
// 1. for in loop
// 2. for each loop
// 3. for of loop

// 4.map

// for in loop

   // for in loop is returns the index of the array

let arr = [451, 32, 53, 42, 56];

for (let i in arr) {
    document.writeln(arr[i] + "<br>");
}

let obj = {
    name: "John",
    age: 30,
    city: "New York"
}

for (let i in obj) {
    document.writeln(obj[i] + "<br>");
}


// for each loop

// for each loop is returns the value and index of the array

let arr1 = [451, 32, 53, 42, 56];

arr1.forEach(function (value, index) {
    document.writeln("for each loop val : "+ value + "  & key : " + index + "<br>");
});

arr1.forEach((val,key) => {document.writeln("for each loop key : " + key + "<br>")});

// for of loop

// for of loop is returns the value of the array

let arr2 = [451, 32, 53, 42, 56];

for (let i of arr2) {
    document.writeln("for of loop val : "+ i + "<br>");
}

//  Map
//  Map is a method like forEach loop
//  Map helps iterate the array or object.

const arr3 = [451, 32, 53, 42, 56];

arr3.map((val) => document.writeln(val *2));


// Task :
/* 
1. login -> enter username and password
2. registration -> enter username and password (save)


3. check Balance -> 1000
4. withdraw -> 100 -> 1000 - 100 = 900
5. deposit -> 100 -> 900 + 100 = 1000
6. logout
*/

user = {
    username: "",
    password: "",
    balance: 0,
}

users =[]


// 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 amstrong number