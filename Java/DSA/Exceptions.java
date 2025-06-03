import java.io.FileNotFoundException;

public class Exceptions {
    public static void main(String[] args) {
        

        // two typw of exception
        // 1. compile time exception
        // 2. runtime exception

        // int x = 10 compile time exception

        try{
            int x = 10 /0;
            System.out.println("Error Happeds");
            try{
                // java code
            }catch(Exception e){
                System.out.println(e);
            }
            
        }catch(Exception e){
            System.out.println(e);
        }finally{
            System.out.println("Finally is working");
        }

    }
}


class NameError extends Exception{
    NameError(){
        super("Name error ");
    }
}