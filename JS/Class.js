// Class
 // Class is a blueprint for creating objects
 // Class is a giant variable that can hold a collection of functions and variables

//syntax
// class class_name{
//     variables
//     functions
//     constructor(){}
// }


// Object
// Object is an instance of a class
// Object is a variable that can hold a collection of functions and variables


// example:

// if we write a function inside a class, then that function is called a method

class Myclass{
    
    hello1() {
        document.writeln("Hello World");
    }

    hello2() {
        document.writeln("Hello Welcome Students");
    }
}

function hello3() {
    document.writeln("Hello Welcome Scope Students");
}

// function call
hello3();

// object creation
let obj = new Myclass();
obj.hello1();
obj.hello2();


class Students{
    // variables
    name;
    age;
    gender;

    // constructor

    // what is constructor?
    // constructor is a special method that is called when an object is created
    // constructor is used to initialize the object
    // constructor is used to set the default values of the object
    constructor(name,age,gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    // methods
    display() {
        let profile = '<br>Name: '+this.name+' <br> Age:'+ this.age + '<br> Gender:'+ this.gender;
        return profile;
    }
}

// object creation

let s1 = new Students("Abhijith",20,"Male");
let s2 = new Students("Steny",20,"Female");
let s3 = new Students("Merin",20,"Female");
let s4 = new Students("Anish",20,"Male");


document.writeln(s1.display());
document.writeln(s2.display());
document.writeln(s3.display());
document.writeln(s4.display());

// Task:
// Create Class Bank
// with acc no, name, balance
// with methods deposit, withdraw, check balance

// Create Objects for 5 customers