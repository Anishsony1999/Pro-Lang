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
    ["red","green","blue"],
    ["chair","table","stool"]
]

document.writeln(furniture[1][1])