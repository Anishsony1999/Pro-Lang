package javalang.dona;

import java.lang.reflect.Array;
import java.util.Random;
import java.util.Scanner;

public class basic {

    public static void main(String[] args) {

        // LOOPS

        //  for loop
        //  while loop
        //  do while loop
        //  for each loop

        for(int i= 1; i <= 10 ; i = ++i + 2){
            // i = i++ ;
            System.out.println(i);
            
        }

        

        //  ++i -> pre increment
        //  i++ -> post increment

        // int j = ++i * 2;
        // System.out.println(j); // 22


        int[] arr= {46,424,64,67,84,44,3,2,323,43};

        System.out.println(arr);

        // [1,3,4,5,2,4,2,1,3,4] , target = 6

        for(int i = 0; i< arr.length ; i++){
            if (arr[i] == 67) continue;
            System.out.print(arr[i] + " ");
        }

        for(int i = 1; i <=3;i++){
            for(int j = i; j <=3 ; j++){
                System.out.println(j + " " + i); // 1 1, 2 1,3 1,
            }
        }

        String[][] arr2 = {
            {"Anish","24","Male"},
            {"Dona","30","Female"},
            {"Arun","30","Male"}
        };

        System.out.println(arr2[2][1]);

        for(int i = 0; i < arr2.length; i++){
            // System.out.println(arr2[i].length);
            for(int j = 0; j < arr2[i].length; j++){
                for(int k = 0 ; k < arr2[i][j].length(); k++){
                    
                }
            }
        }

        // String
        // String is immutable
        // String is a squence of characters
        // String is a Object
        // String is indexed starting from 0
        // String object are stored in heap memory ( String pool )

        // Creating String

        String str1 = "anish"; // String Literal
        String str4 = "Anish";
        String str2 = new String("Dona"); // String Object

        System.out.println(str1.charAt(2));
        
        
        String str3 = new String("Anish");

        // == operator compares the address of the object

        if (str4.equals(str1)){
            System.out.println("Equal");
        }
        
        // String Methods

        // length()
        // charAt()
        // substring()
        // equals()
        // equalsIgnoreCase()
        // toLowerCase()
        // toUpperCase()
        // trim()
        // concat()
        // replace()
        // split()
        // indexOf()  
        // lastIndexOf()
        // contains()
        // startsWith()
        // endsWith()

        String substring = str1.substring(0,3);
        System.out.println(substring); // Ani

        String newString = "    this appoinment id=1896 and date=23  " ;

        // for(int i=0 ; i <newString.length(); i++){
        //     if ( newString.charAt(i)>='0' && newString.charAt(i)<='9'){
        //         System.out.print(newString.charAt(i));
        //     }
        // }

        boolean fount = false;
        for(int i=0 ; i <newString.length(); i++){

            if((newString.charAt(i)>='0' && newString.charAt(i)<='9')){
                fount = true;
                System.out.print(newString.charAt(i));
            }

            if (fount && newString.charAt(i) == ' '){
                break;
            }
            i++;
        }
        
        // equalIgnoreCase()

        if(str1.equalsIgnoreCase(str4)){
            System.out.println("Equal");
        }

        System.out.println(newString.toLowerCase());
        System.out.println(newString.toUpperCase());

        
        System.out.println(newString.trim());
        
        String fname = "Anish";
        String lname =" Sony";
        System.out.println(fname.concat(lname));
        String fullName  = fname + lname;
        System.out.println(fullName);


        System.out.println(fullName.replace("A","S"));
        System.out.println(fullName);

        System.out.println(fullName.indexOf("S"));

        System.out.println(fullName.lastIndexOf("ny")); // Anish Sony

        System.out.println(fullName.startsWith("Anish"));

        System.out.println(fullName.endsWith("y"));

        System.out.println(fullName.contains("Anish"));

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string");
        String str = sc.next();

        // hello world. -> .dlrow olleh
        // Hello World. -> .World Hello



        sc.close();
        
    }
}
