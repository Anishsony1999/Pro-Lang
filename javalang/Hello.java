import java.util.Scanner;

class Hello {
    public static void main(String[] args){
    
        String userName = "Anish";
        int pass = 123;
        double balance = 0;

        Scanner sc  = new Scanner(System.in);

        System.out.println("Enter Your User Name");
        String uName = sc.next();
        
        System.out.println("Enter Your User Pass");
        int uPass = sc.nextInt();

        if(userName.equals(uName) && pass == uPass){
            boolean q = true;
            while (q) {
            
                System.out.println("1,Depo\n2,With\n3,balnce\n4,exit");
                int option = sc.nextInt();

                switch (option) {
                    case 1:
                        System.out.println("Depo u r amout");
                        int amout = sc.nextInt();
                        balance = balance + amout;
                        System.out.println("Balance : "+ balance );
                        break;
                
                    case 2:
                        System.out.println("withdow amout");
                        int wAmout = sc.nextInt(); 

                        if(wAmout > balance){
                            System.out.println("Warring");
                        }else{
                            balance = balance - wAmout;
                            System.out.println(balance);
                        }
                        break;
                    case 3:
                        System.out.println(balance);
                        break;
                    case 4:
                        q = false;
                        System.out.println("exit the prog");
                        break;
                    default:
                        break;
                }
            }
        }

    }

}