package javalang.dona;

import java.util.Random;

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

        // Creating String

        String str1 = "Anish"; // String Literal
        String str2 = new String("Dona"); // String Object

        System.out.println(str1.charAt(2));
        
        
        String str3 = new String("Anish");

        Random random = new Random();
        int x = random.nextInt(1,11);
        
    }
}
