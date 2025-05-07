import java.util.Scanner;

class Hello {
    public static void main(String[] args){
    
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter color");
        String color = sc.next();
        switch(color){
            case "blue":
            System.out.println("Blue");
            break;

            case "yellow" :
            System.out.println("Yellow");
            break;

            case "pink": 
            System.out.println("Pink");
            break;

            case "red" :
            System.out.println("Red");
            break;

            default:
            System.out.println("Nothing");
        }

        
    }

}