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

document.writeln(kids[2]["name"])