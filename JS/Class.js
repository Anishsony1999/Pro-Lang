// Class
 // Class is a blueprint for creating objects
 // Class is a giant variable that can hold a collection of functions and variables

//syntax
// class class_name{
//     variables
//     functions
//     constructor(){}
// }


// Object:
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

// Inheritance :- 

// Inheritance is the one way sharing
// sharing members of one class to another class
// Inheritance is a mechanism in which one object acquires all the properties and behaviors of a parent object.
// Inheritance is used to achieve re-usability of code.

// Types of Inheritance:
// 1. Single Inheritance
// 2. Multiple Inheritance
// 3. Multilevel Inheritance
// 4. Hierarchical Inheritance
// 5. Hybrid Inheritance


class Parent{
    x;

    constructor(x){
        this.x = x;
    }
    sum(){
        return this.x * this.x;
    }
    hello(){
       document.writeln("Hello World");
    }
}


class Child extends Parent{

    constructor(x){
        // let p1 = new Parent(x);
        super(x);
    }
    // super() is used to call the near by parent class constructor and methods
    y =20;
}

// object creation

let c1 = new Child(20);
document.writeln("Child class y value : " + c1.y);
document.writeln("Parent class x value : " + c1.x); 
c1.hello();


// Polymorphism

// poly means many
// morph means forms

// polymorphism is many-forms

// Overriding:
// Overriding is a mechanism in which one class acquires all the properties and behaviors of a parent class.
// Overriding is used to achieve re-usability of code.
// Overriding is used to achieve run-time polymorphism.
// and is happens in inheritance.

class A {
    hello(){
        document.writeln("<br> Hello World from parent class <br>");
    }
}

class B extends A{
    hello(){
        document.writeln("<br> Hello Students from child class");
    }
}

let b1 = new B();
b1.hello();