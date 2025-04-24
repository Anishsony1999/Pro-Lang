package javalang;

import java.util.ArrayList;

public class Data {
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
            ArrayList<Integer> al = new ArrayList<>();

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
        }

}
