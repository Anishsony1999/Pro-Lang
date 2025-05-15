public class Array {
    public static void main(String[] args) {
        String str = "jytrgy";
        
        System.out.println(pali(str));
    }

    public static String pali(String str){
        int left = 0;
        int right = str.length()-1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return "This is not a palidrome";
            }
            left++;
            right--;
        }
        return "This is a Palidrome";
    }
}


// 1) Hello World -> dlroW olleH
// 2) Hello World -> olleH dlroW