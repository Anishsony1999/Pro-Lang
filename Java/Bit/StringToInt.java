public class StringToInt {
    public static int stringToInt(String input) {
		
        int ans = 0;
        int p2 = 1;
        for(int i = input.length()-1 ; i >=0 ; i--){
            if(input.charAt(i) == '1'){
                ans += p2;
            }
            p2 *= 2;
        }

        return ans;
	}
    public static void main(String[] args) {
        String s = "1101";
        System.out.println(stringToInt(s));
    }
}
