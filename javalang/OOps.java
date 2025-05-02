package javalang;

public class OOps {
    // OOps  - Object Oriented Programming

    // What is OOps ?
    // this is a programming paradigm that is based on the concept of objects.


    // Createing real Home 
    // we need a plan - engineer - blueprint
    // we need a builder - constructor team
    // we need a material - object
    
    
    // Jithu - home
    // jithu  will the same engineer - blueprint
    // jithu  will the same builder - constructor team
    // jithu  will the same material - object

    // Sandra - home
    // sandra  will the same engineer - blueprint
    // sandra  will the same builder - constructor team
    // sandra  will the same material - object

    // oops :-
    // 1) Class - blueprint 
    // 2) Object - home
    // 3) Constructor - builder team


    // oops :
    // 1) Class
    // 2) Object

    // pillar of oops :
    // 3) Inheritance
    // 4) Polymorphism
    // 5) Abstraction
    // 6) Encapsulation

    public static void main(String[] args) {
        // create object of String

        String str = new String("Hai bro");

        // //creating object of Home class
        // Home abiBhavan = new Home();

        // abiBhavan.room = 4;
        // abiBhavan.color = "pistaGreen";
        // abiBhavan.lights = "white";
        // abiBhavan.floor = 3;

        // System.out.println(abiBhavan.room);


        // Home jithuBhavan = new Home();
        // jithuBhavan.room = 3;
        // jithuBhavan.color = "white";
        // jithuBhavan.lights = "white";
        // jithuBhavan.floor = 3;

        // System.out.println(jithuBhavan.room);

        // Home sandraBhavan = new Home();
        // sandraBhavan.room = 4;
        // sandraBhavan.color = "white";
        // sandraBhavan.lights = "white";
        // sandraBhavan.floor = 3;

        // System.out.println(sandraBhavan.room);

        // Creating Home Object using parameterized constructor

        Home abiBhavan = new Home(4,"pistaGreen","white",3); 
        Home jithuBhavan = new Home(3,"white",3);
        Home sandraBhavan = new Home();

        System.out.println(abiBhavan.room);
        System.out.println(jithuBhavan.room);
        System.out.println(sandraBhavan.room);

    }

}


// class syntax :
// class ClassName{
//     // code
// }


// this is a data type (Home)

class Home{
    int room ;
    String color;
    String lights;
    int floor;

    Home(){
        System.out.println("Home is created");
    }

    Home(int room,String color,String lights,int floor){
        this.room = room;
        this.color = color;
        this.lights = lights;
        this.floor = floor;
    }

    Home(int room,String color,int floor){
        this.room = room;
        this.color = color;
        this.floor = floor;
    }

    // functions in java or OOPs is called methods

    void tvOn(){
        System.out.println("TV is ON");
    }

    void tvOff(){
        System.out.println("TV is OFF");
    }

    void tarnOnTheFan(){
        System.out.println("Fan is ON");
    }

    void tarnOffTheFan(){
        System.out.println("Fan is OFF");
    }

    void lightOn(){
        System.out.println("Light is on");
    }

    void lightOff(){
        System.out.println("Light is off");
    }


    int sum(int x,int y){
        return x+y;
    }

    public String addName(String fname,String lname){
        return fname + " " + lname;
    }

}

// Class :-
// 1) Class is a blueprint of an object.
// 2) class have meathods, properties , constructors, variables, etc.



// Object :-

// 1) Object is an instance of a class.
// 2) Object is a real world entity.


// Access Modifiers :
// 1) public
// 2) private
// 3) protected
// 4) default

// public : 
// public is an access modifier that is used to make a class, method, variable, etc. accessible from any where.
// if we use a public access modifier then it is accessible from any where in our project.

// private : 
// private is an access modifier that is used to make a class, method, variable, etc. accessible from the same class.
// if we use a private access modifier then it is accessible from the same class only.


// protected : 
// protected is an access modifier that is used to make a class, method, variable, etc. accessible from the same package .
// if we use a protected access modifier then it is accessible from the same package only.

// default : 
// default is an access modifier that is used to make a class, method, variable, etc. accessible from the same package.
// if we use a default access modifier then it is accessible from the same package only.


// Constructor :-
// 1) Constructor is a special method that is used to initialize the object.
// 2) Constructor is a method that is called when an object is created.
// 3) Constructor name is same as class name.
// 4) Constructor doesn't have any return type.

    // 1) Default Constructor :-
        // Default Constructor is a constructor that is called when an object is created.
        // default ""    is created by java compiler.
        // if we don't create any constructor then java compiler will create a default constructor.
        // if we declare a class then java compiler will create a default constructor.


    // 2) Parameterized Constructor :-

        // Parameterized Constructor is Constructor that takes parameters.

        // Constructor Overloading :-
            // Constructor Overloading is a feature of java that allows a class to have more than one constructor.
    // 3) Copy Constructor :-
        // Copy Constructor is a constructor that takes an object of the same class as a parameter.
        // Copy Constructor is used to create a copy of an object.

        // Home(int room,String color,String lights,int floor){
        //     this.room = room;
        //     this.color = color;
        //     this.lights = lights;
        //     this.floor = floor;
        // }

        // Home(Home obj){
        //     this.room = obj.room;
        //     this.color = obj.color;
        //     this.lights = obj.lights;
        //     this.floor = obj.floor;
        // }

    // 4) Chain Constructor :-
        // Chain Constructor is a constructor that calls another constructor of the same class.

        // Home(int room,String color,String lights,int floor){
        //     this(room,color,floor);
        //     this.lights = lights;
        // }


    // Inheritance :-
    // 1) Inheritance is a feature of java that allows a class to inherit the properties of another class.
    // 2) Inheritance is oneway shareing.
    // 3) in class we use extends keyword to inherit the properties of another class.
    // 4) in interface we use implements keyword to inherit the properties of another interface.
     
    // Inheritance is 5 type : 
            // 1) Single Inheritance - single parent single child
            // 2) Multilevel Inheritance - multiple parent multiple child
            // 3) Hierarchical Inheritance - single parent multiple child
            // 4) Multiple Inheritance - multiple parent single child
            // 5) Hybrid Inheritance - Multiple Inheritance + Hierarchical Inheritance

    

        