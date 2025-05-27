// if , else , else if 

// if (condition) {}

// num = prompt("Enter a number"); // '10'
// let num1 = Number(num); // 10

// if (num1 >5) {
//     console.log("Number is greater than 5");
// }
// // else{}
// if (num1 >5) {
//     document.writeln(num1);
//     document.writeln("Number is greater than 5");
// }else{
//     document.writeln(num1);
//     document.writeln("Number is less than 5");
// }

// ============== else if ============
// if (condition) {}
// else if (condition) {}
// else {}

// let marks = prompt("Enter your marks");// '78'
// marks = Number(marks);

// if (marks >= 90) {
//     document.writeln("Grade A");
// }
// else if (marks >= 80) {
//     document.writeln("Grade B");
// }else{
//     document.writeln("Grade C");
// }



num1 = Number(prompt("Enter a number"));
num2 = Number(prompt("Enter a number"));

action = prompt("Enter an action");

if (action == "+") {
    document.writeln(num1 + num2);
}else if (action == "-") {
    document.writeln(num1 - num2);
}else if (action == "*") {
    document.writeln(num1 * num2);
}else if (action == "/") {
    document.writeln(num1 / num2);
}else{
    document.writeln("Invalid action");
}


// ======= switch case ========

// switch (condition) {
//     case value1:
//         // code block
//         break;
//     case value2:
//         // code block
//         break;
//     default:

switch (action) {
        case "+" :
            document.writeln(num1 + num2);
            break;
        case "-" :
            document.writeln(num1 - num2);
            break;
        case "*" :
            document.writeln(num1 * num2);
            break;
        case "/" :
            document.writeln(num1 / num2);
            break;
        default:
            document.writeln("Invalid action");
}

// enter a month number and print the month name
// 1 - January

