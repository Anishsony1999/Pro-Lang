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



// hello(); // function calling

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

// let x = Number(prompt("Enter first number"));
// let y = Number(prompt("Enter second number"));

// let z = sum3(x,y);
// document.writeln("Sum is : " + z);

// for(let i = 100 ; i >=0 ; i-=2){
//     document.writeln(i);
// }



// let x = Number(prompt("Enter a number"));

//5 -> 1 * 5 = 5 to 10 * 5 = 50 ;

// if (x > 5){
//     function xy(){}
// }else{
//     function yz(){}
// }

// variable functions

// let sum = function(x,y){
//     return x + y;
// }

// document.writeln(sum(10,20));

// Arrow functions

let sum4 = (x,y) => x + y;

document.writeln(sum4(10,20));


function hello(){
    document.writeln("hello world <br>");
}

function calHello(){
    hello();
}

calHello();


// recursive function
// function calling itself
y = 10;
function mul(x,y){
    if (y == 0) return;
    mul(x,y-1); 
    document.writeln(x + " * " + y + " = " + x * y + "<br>"); 
}
x = Number(prompt("Enter a number"));
mul(x,y);


