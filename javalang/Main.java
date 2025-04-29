package javalang;

class Main {
    
    public static void main(String[] args) {

        Home AbhBhavan = new Home(1, "white", "warm", 3);
        Home BabiBhavan = new Home(4, "white", "white", 3);

        
        AbhBhavan.tvOn();
        BabiBhavan.tarnOnTheFan();

        AbhBhavan.lightOff();
        AbhBhavan.tarnOffTheFan();



    }
}