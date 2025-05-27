// what is loops?
// loops are used to repeat a block of code multiple times.
// there are two types of loops in javascript.
// 1. for loop
   // for in loop
   // for each loop
// 2. while loop
    // do while loop


// document.writeln("hello world" + "<br>");
// for loop

// for (initialization; condition; increment/decrement) {}

for (let i = 1; i <= 100 ; i++){
    document.writeln(i + ", hello world" + "<br>");
}


// while loop

// while (condition) {}

let i = 1;
while (i <= 10) {
    document.writeln(i + ", hello world" + "<br>");
    i++;
}

// do while loop

// do {} while (condition);

let j = 1;
do {
    document.writeln(j + ", hello world" + "<br>");
    j++;
} while (j <= 10);


// Task:
// 1. print all the even numbers from 1 to 100 using for loop
// 2. palindrome : amma , malayalam 