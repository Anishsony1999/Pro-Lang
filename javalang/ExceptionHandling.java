package javalang;

import java.io.FileNotFoundException;

public class ExceptionHandling {
    public static void main(String[] args) {
        // Throw Keyword
        // throw is used to throw an exception.
        // Only one Object can be thrown at a time.

        int x = 13; // 16 bits [0000000000001011]


        if (x == 10){
            throw new ArithmeticException("File not found");
        }
        
    }

}

class A {
    public void add(int x, int y){
        int z = x + y;
        System.out.println(z);
    }
}

final class B extends A {
    @Override
    public void add(int x, int y){
        int z = x + y;
        System.out.println(z);
    }
}

// finalize is the meathod -> only for garbage collection

// finalize vs final vs finally