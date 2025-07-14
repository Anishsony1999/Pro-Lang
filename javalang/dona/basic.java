package javalang.dona;

public class basic {

    public static void main(String[] args) {

        String[] names = {"Dona","Anish","Sony"};

        for(String i : names){
            System.out.println(i);
        }

        System.out.println(names[0]);

        // Two Dimensional Array
        int[][] nums = new int [3][3];
        int[][] nums2 ={
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        System.out.println(nums2[2][2]);



        // [
        //  [1,2,3],
        //  [4,5,6],
        //  [7,8,9]
        // ]


        System.out.println(nums.length);
    }
}
