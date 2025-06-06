public class And {
    public static void main(String[] args) {
        int x = 13 & 7; // 1101 & 0111 = 0101 = 5
        int y = 13 | 7; // 1101 | 0111 = 1111 = 15
        int z = 13 ^ 7; // 1101 ^ 0111 = 1010 = 10

        int a = 13 >> 1 ; // 1101 >> 1 = 0110 = 6
        int b = 13 >> 2 ; // 1101 >> 2 = 0011 = 3

        int max = Integer.MAX_VALUE;
        System.out.println(max);
    }
}
