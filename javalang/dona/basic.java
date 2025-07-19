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



        // hello world. -> .dlrow olleh
        // Hello World. -> olleH .dlroW


        String name = "Dona";
        System.out.println(name.charAt(0));
        
        // String is immutable so we cant change the value of the string
        // name.charAt(0) = 'A'; // Error

        name = "Anish";
        System.out.println(name);

        String rev= "";

        for(int i = name.length()-1; i>=0 ; i--){
            rev = rev + name.charAt(i);
        }

        // if you use += operator then it will create a new object in the heap memory
        
        // StringBuffer 
        // STringBuffer is mutable 
        // this is same as String but StringBuffer is mutable


        StringBuffer sb = new StringBuffer("Anish");

        System.out.println(sb.getClass());

        sb.append("Sony");
        sb.insert(0, "Hello");
        sb.reverse();
        sb.delete(0, 5);

        // append();
        // insert();
        // delete();
        // reverse();

        System.out.println(sb);

        // String Builder 
        // StringBuilder is mutable
        // StringBuilder is faster than StringBuffer
        // StringBuilder is run in single thread
        // StringBuilder is not thread safe
        // StringBuilder is not synchronized
        
        StringBuilder sb2 = new StringBuilder("");
        sb2.append("Anish");
        sb2.insert(0, "Hello");
        sb2.reverse();


        // while loop

        int i = 1;

        while ( i <= 10 ){
            System.out.println(i);
            i++;
        }
        
        // endless loop
        while (true){
            System.out.println("Hello");
            break;
        }

        // do while loop

        int j = 13;

        do{
            System.out.println(j);
            j++;
        }while(j <= 10);

        // palindrome;
        // String -> Amma , Malayalam ,( a man, a plan, a canal: panama! )

        // for each loop ?
        // arrays read, objects read and collections read

        int[] arr3 = {4,57,5,7,3,43,3};

        for(int k : arr3){
            System.out.println(k);
        }

        // revers a integer 
        // num = 12 -> 21
        // num = -12 -> -21

        

    }
}
