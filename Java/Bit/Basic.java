
class Basic{

    public static String bitToString(int x){
        StringBuffer sb = new StringBuffer("");

        while(x > 0){
            if (x%2 == 1)sb.append("1");
            else sb.append("0");
            x = x/2;
        }
        sb.reverse();
        return sb.toString();
    } 

    public static void main(String[] args) {
        int x = 13;
        System.out.println(bitToString(x));
    }
}