import java.util.Scanner;

class Hello {
    public static void main(String[] args){
        System.out.println("Hello World");

        int x = 10;
        Scanner sc= new Scanner(System.in);

        long num = 999999999;
        System.out.println("Enter a number");
        // int y = Integer.parseInt("10");
        int y = sc.nextInt();
        // int z =Integer.parseInt("22");
        System.out.println("Enter a num");
        int z = sc.nextInt();
        System.out.println(y+z);

    }

}