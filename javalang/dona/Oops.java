package javalang.dona;

public class Oops {
    // oops -> object oriented programming system

    // class 
    // object
    
    // piller of oops
    // 1. inheritance
    // 2. polymorphism
    // 3. encapsulation
    // 4. abstraction

    // class -> class is the blueprint of the object
    // object -> object is the instance of the class, object are create in runtime


    // constructor -> meathod -> access modifiers

    // access modifiers -> public , private , protected , default

    // public -> can be accessed from anywhere (in same package and outside package)
    // private -> can be accessed only in the same class
    // protected -> can be accessed in the same package and outside package (in sub class)
    // default -> can be accessed in the same package (in same class and sub class)


    public static void main(String[] args) {
    
        // firbinal number
        int x = 0;
        int y = 1;
        // 0,1,1,2,3,5,8,13

        for(int i = 1; i<=10; i++){
            System.out.println(x);
            
            int temp = x + y ;
            x = y;
            y = temp;
        }
        
    }
}
class Home{
    String color;
    int room ;
    int chairs;
}


// pillers of oops 

// 1, inheritance
// 2, polymorphism
// 3, encapsulation
// 4, abstraction


// 1, inheritance:
// inheritance is a one way sharing 
// ita parent child relation ship

// child class can access parent class methodas and variables
// parent class can not access child class methodas and variables

// we use a keyword extends to create inheritance

// single inheritance

// polymorphism :
// poly meams many
// morph means forms

// many + forms  = polymorphism

// type of polymorphism:
// 1, compile time polymorphism (overloading)
// 2, runtime polymorphism (overriding)

// overriding :
// its happens in runtime
// same method name and same number of arguments
// its happens in inheritance (parent child relation ship)


// abstraction:
// its a process of hiding the implementation details and showing only the functionality to the user

// using abstract class and interface we can create abstraction

// interface:
// in interface all the method are public abstract and all the variables are final and static
// we can not create object of interface
// we can implement interface using implements keyword
// we con't inherit interface using extends keyword
// we can inherit multiple interface.
// also we can write method in interface using default keyword