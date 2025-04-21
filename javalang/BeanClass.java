package javalang;

// Exception Handling

public class BeanClass {

    public static void main(String[] args) {

        // What is exception ?
        // Exception is an event that disrupt the normal flow of the program.

        // try block
        // try block are used to enclose the program statements that might throw an exception.

        // catch block
        // catch block are used to handle the exception.

        // syntax :
        // try{
        //     // code
        // }catch(Exception e){
        //     // code
        // }

        // exception 2 type 
        // 1) checked exception
        // 2) unchecked exception

        // checked exception : compile time exception
        // unchecked exception : run time exception

        int x = 10;
        int y = 0;

        try{  
            try{
                int a = 10;
                int b = 0;
                int c = a/b;
            }catch(Exception e){
                System.out.println(e);
            }
            int z = x/y;
        System.out.println(z);

        }catch(Exception e){
            System.out.println(e);
        }
        // finally block
        // finally block are used to execute the code regardless of the exception.
        // database closing , file closing
        finally{
            System.out.println("finally block");
        }

    }

}
