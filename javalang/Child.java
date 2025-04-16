package javalang;

public class Child extends Parent{
    int childIncome = 3000;

    void sum(int x ,int y){
        System.out.println( x + y);
    }

    void sum(int x, float y){
        System.out.println(x + y);
    }

    void sum(int x ,double y){
        System.out.println( x + y);
    }

    void sum(int x ,int y, int z){
        System.out.println( x + y + z);
    }

    void sum(int x, double y, int z){
        System.out.println(x + y + z);
    }
}
