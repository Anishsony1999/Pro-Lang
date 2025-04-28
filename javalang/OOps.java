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
        Home jithuBhavan = new Home(3,"white","white",3);
        Home sandraBhavan = new Home(4,"white","white",3);

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

    // constructor
    // method

    Home(){
        System.out.println("Home is created");
    }

    Home(int room,String color,String lights,int floor){
        this.room = room;
        this.color = color;
        this.lights = lights;
        this.floor = floor;
    }
}

// Class :-
// 1) Class is a blueprint of an object.
// 2) class have meathods, properties , constructors, variables, etc.


// Object :-

// 1) Object is an instance of a class.
// 2) Object is a real world entity.

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