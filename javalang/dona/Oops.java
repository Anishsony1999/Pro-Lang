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
    // object -> object is the instance of the class

    public static void main(String[] args) {
        // int x;
        // Home bh = new Home();
        // Home sony = new Home();
        // // System.out.println(x); 

        // System.out.println(bh.color);
        // System.out.println(sony.color);
        int arr[]= {1,3,5,2,4,9};
        int k=0;
        for (int i=0; i <arr.length; i++){
            k=arr[i];
            System.out.println("loop i : " + k);
            for (int j= i+1; j<arr.length; j++)
                k = k+ arr[j];
                System.out.println(k);
                if (k == 6) {
                    System.out.println(i + ", " + k);
                }
            
        }
    }
}
class Home{
    String color;
    int room ;
    int chairs;
}



