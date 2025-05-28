/*

Functions:
    A fuction is a variable that stores a group of statements.
    A function is a block of code that performs a specific task.
    A function is a reusable block of code.
    functions help to avoid scripting redundancy.

    User defined functions
    Built in functions - Done


    User defined functions:

        function function_name() {
        }

        function calling:
            function_name();
*/

function hello(){
    document.writeln("hello world");
}

hello(); // function calling

function sum(){
    let x = Number(prompt("Enter first number"));
    let y = Number(prompt("Enter second number"));
    let z = x + y;
    document.writeln("Sum is : " + z);
}

// sum();

// function with parameters
// function call must be in the same order as the parameters.

function sum2(x,y){
    let z = x + y;
    document.writeln("Sum is : " + z);
}

// let y = Number(prompt("Enter second number"));
// let x = Number(prompt("Enter first number"));

// sum2(x,y);

// function with return value

function sum3(x,y){
    let z = x + y;
    return z;
}

let x = Number(prompt("Enter first number"));
let y = Number(prompt("Enter second number"));

let z = sum3(x,y);
document.writeln("Sum is : " + z);