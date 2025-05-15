public class Ami {
    public static void main(String[] args) {
        Home sk = new Home("White",3,2);
        Home ab = new Home("Blue",5,10);
        Home av = new Home("Pink",10,5);
        sk.lightOn();
    }
}

class Home {

    String color;
    int room;
    int floor;
    
    Home(String colorr,int roomm , int floorr){
        this.color = colorr;
        this.room = roomm;
        this.floor = floorr;
    }

    void lightOn(){
        System.out.println("light will on ");
    }

    void lightOff(){
        System.out.println("Light Will Off");
    }
}