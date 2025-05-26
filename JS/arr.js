// Arrays

// A Collection of Values/data in variables called arrays or array variables.


// empty array
var arr_name = [];
var arr_name1 = new Array();

// array with value
var arr_name2 = ["name1","name2","name3"]; 
var arr_name3 = new Array("name1,name2,name3");


name1 ="ncoic";
name2 = "aki";
name3 = "ind";

names = [name1,name2,name3];// len (3) | last index len-1 (2)

// single dimensional array

names = ["merin" , "sooraj" ,"abhijith","anish"];
names[3] = "anisha";

document.writeln("<h1>"+ names+ "</h1>");
document.writeln("<h1>"+ names[2] + "</h1>");


// array in side array 
//two-dimenstional arrays

var furniture = [
    ["red","green",["arra","afyfa",["anish"]]],
    ["chair","table","stool"]
]

document.writeln(furniture[0][2][2][0])

// JSON - javascript object notation 

var person = [
    "anish", // 0
    "sony", // 1
    "tvm"  // 2
]

var person1 = {
    name : "anish", // 0 - name
    age : 24,
    location : "tvm"
}

document.writeln(person[1]);
document.writeln(person1["age"]);
document.writeln(person1.age);


var kids = [
    {
        name : "anish",
        age : 24,
        location : "tvm"
    },
    {
        name : "sooraj",
        age : 24,
        location : "tvm"
    },
    {
        name : "merin",
        age : 24,
        location : "tvm"
    }
]

document.writeln(kids[2]["name"]);



// Array Handling Functions

var names = ["merin","sooraj","anish"];
console.log(names);

// push() - add value at the end of array

names.push("Abhijith");
console.log("push function : " + names);

// pop() - remove value from the end of array
names.pop();

console.log("pop function : " + names);

// unshift() - add value at the start of array

names.unshift("abhijith");
console.log("unshift function : " + names);

// shift() - remove value from the start of array
names.shift();

console.log("shift function : " + names);

names.shift();

console.log("shift function : " + names);

// =========================================

// Array to String 

// toString() - convert array to string

console.log(names);
console.log("using toString() : " +names.toString());

// join() - convert array to string
console.log("using join() : " +names.join(" "));

// =============================================
// Sting to Array

// split() - convert string to array

var str = "merin,sooraj,abhijith,anish";
let arr2 =[];
arr2 = str.split(',');
console.log(arr2);

// find() - find the index of the value

console.log(arr2);
console.log("using find() : " + names.find((name)=> name == "anish"));

// filter() - filter the array
var price = [30,40,24,24,576,4,37,64,32,54];
console.log("using filter() : " + price.filter((price)=> price < 40));

// includes() - check if the value is present in the array return true or false
console.log("using includes() : " + names.includes("anish"));

//indexOf() - check if the value is present in the array return index or -1
console.log("using indexOf() : " + names.indexOf("sooraj"));



// sort() - sort the array
price = price.sort((a,b)=> a-b) // ascending order
console.log("using sort() :  " + price); 

console.log("using sort() : "+ names.sort()); // strings
