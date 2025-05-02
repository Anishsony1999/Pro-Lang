package javalang;

import java.util.ArrayList;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Data {

    public int sum (int x, int y){
        return x+y;
    }

    // Wrapper Class in Java
    // Wrapper Class is a class that wraps a primitive data type.

    // Primitive Data Type : int, char, boolean, float, double, byte, short, long
    // Wrapper Class : Integer, Character, Boolean, Float, Double, Byte, Short, Long

    // Collections in Java

    // What is Collection ?
    // Collection is a group of objects.
    // Collection is a group of objects that are stored in a single unit.
    // Collection is a group of objects that are stored in a single unit and can be accessed by a single name.

    int[] arr = {1,2,3,4,5,6,7,8,9,10};
    int[] arr1 = new int[10];

    // Collections in Java are of 4 types :(Interfaces)
    // 1) List 
    // 2) Set
    // 3) Map
    // 4) Queue

    // 1) List : 
        // 1) ArrayList
        // 2) LinkedList
        // 3) Vector
        // 4) Stack

    // 2) Set : 
        // 1) HashSet
        // 2) LinkedHashSet
        // 3) TreeSet

    // 3) Map : 
        // 1) HashMap
        // 2) LinkedHashMap
        // 3) TreeMap

    // 4) Queue : 
        // 1) PriorityQueue

    
        // List Interface
        // List Interface is a child interface of Collection Interface.
        // List has dynamic array.

        // Note:-
        // We can't craete object of interface. but we can create object of class that implements interface.

        // ArrayList Class :-

        public static void main(String[] args) {
            int[] arr = new int[10];

            // ArrayList declaration
            ArrayList<Integer> al = new ArrayList<>(){{add(10);add(20);}};

            

            al.add(10);
            al.add(20);
            al.add(20);
            al.add(300);

            // ArrayList Meathods
            // 1) add() : add element in ArrayList
            // 2) get() : get element from ArrayList
            // 3) remove() : remove element from ArrayList
            // 4) size() : return size of ArrayList
            // 5) clear() : clear ArrayList
            // 6) set() : set element in ArrayList

            al.remove(al.get(1));

            al.set(1,200);

            System.out.println("index of 0 : "+al.get(0));
            // al.clear();
            System.out.println("List of ArrayList : "+al);
            System.out.println("Size of ArrayList : "+al.size());

            // ArrayList :
            // allows duplicate elements
            // maintains insertion order

            User user = new User();
            user.name = "Anish";
            user.age = 24;

            System.out.println("Object : " + user);

            List<User> al1 = new ArrayList<>();
            al1.add(user);
            System.out.println(al1.toString());

            //Object class
            Object ob = new Object();

            // Set Interface
            // Set Interface is a child interface of Collection Interface.

            // HashSet Class :-
            // HashSet is a class that implements Set Interface.
            // HashSet is a class that implements Set Interface and it is a part of Collection Framework.
            // HashSet is a class that implements Set Interface and it is a part of Collection Framework and it is a part of java.util package.

            Set<String> hs = new HashSet<>();

            // difference between ArrayList and HashSet
            // ArrayList allows duplicate elements but HashSet doesn't allow duplicate elements.
            // ArrayList maintains insertion order but HashSet doesn't maintain insertion order.

            // Set allows null values but HashSet doesn't allow null values.

            hs.add("Anish");
            hs.add("binoja");
            hs.add("Anish");
            hs.add("aaa");

            // Set interface methods

            // 1) add() : add element in HashSet
            // 2) remove() : remove element from HashSet
            // 3) size() : return size of HashSet
            // 4) clear() : clear HashSet
            // 5) contains() : check element is present in HashSet or not
            // 6) isEmpty() : check HashSet is empty or not

            // we cont use get() and set() methods in HashSet
            // because HashSet doesn't maintain insertion order.

            System.out.println("List of HashSet : "+hs);


            // III ) Map Interface :-

            // Map Interface is not a child interface of Collection Interface but it is a part of Collection Framework and it is a part of java.util package.

            // Map is unique
            // Map is Unordered Collection of key-value pairs. like dictionary, Json(JavaScript Object Notation)
            // Map Dosn't allow duplicate keys but it allows duplicate values.
            // Map Allows null keys and null values.


            // Map Methods :-
            // 1) put() : add element in Map
            // 2) get() : get element from Map 
            // 3) remove() : remove element from Map 
            // 4) size() : return size of Map 
            // 5) clear() : clear Map 
            // 6) containsKey() : check key is present in Map or not 
            // 7) containsValue() : check value is present in Map or not 
            // 8) isEmpty() : check Map is empty or not 
            // 9) keySet() : return all keys of Map 
            // 10) values() : return all values of Map 

            // Map<Key , Value>

            Map<String, Integer> map = new HashMap<>();
            // int is primitive type but we use Integer because Integer is a wrapper class of int.
            map.put("Anish", 24);
            map.put("Binoja", 25);
            map.put("Anish", 26); // Duplicate key is not allowed in Map.
            map.put(null,null); // null key is allowed in Map.
            map.put("anish",24); // Duplicate value is allowed in Map.

            System.out.println("List of Map : "+map);
            System.out.println("Value of Anish : "+map.get("Anish"));
            System.out.println("Size of Map : "+map.size());
            System.out.println("Keys of Map : "+map.keySet());
            System.out.println("Values of Map : "+map.values());
            System.out.println("Is Map empty : "+map.isEmpty());
            System.out.println("Is Map contains key Anish : "+map.containsKey("Anish"));

            //Dictionary
            // Dictionary is a class that implements Map Interface.
            // Dictionary is a class that implements Map Interface and it is a part of Collection Framework.
            
            Dictionary<String,String> dict = new Hashtable<>();

            // Dictionary Methods :-
            // 1) put() : add element in Dictionary
            // 2) get() : get element from Dictionary 
            // 3) remove() : remove element from Dictionary 
            // 4) size() : return size of Dictionary 
            // 5) clear() : clear Dictionary 
            // 6) containsKey() : check key is present in Dictionary or not 
            // 7) containsValue() : check value is present in Dictionary or not 
            // 8) isEmpty() : check Dictionary is empty or not 
            // 9) keySet() : return all keys of Dictionary 
            // 10) values() : return all values of Dictionary 

        }

}

class User{
    String name;
    int age;

    @Override
    public String toString() {
        return   name ;
    }
}


// Java Meathods

// Sytax :

// access_modifier return_type method_name(parameters){
//    code
//  }

