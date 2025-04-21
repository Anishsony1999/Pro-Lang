package javalang;

// Thread

// What is Thread ?
// Thread is a lightweight process.
// Thread is a part of a process.

// what is main thread ?
// main thread is a thread that is created by the JVM.

// what is process ?
// process is a program that is being executed.

// tread life cycle ?
// 1) New
// 2) Runnable
// 3) Running
// 4) Blocked / Sleeping
// 5) Dead

// What is multithreading ?
// Multithreading is a process of executing multiple threads simultaneously.

// how to create a thread ?
// 1) by extending Thread class
// 2) by implementing Runnable interface

public class Threadd {
    public static void main(String[] args) {
        
        MyThread t = new MyThread(); // Thread class
        t.start();

        MyThread2 t2 = new MyThread2(); // Runnable interface
        Thread t3 = new Thread(t2);  // Thread class
        t3.start();

        // labmda expression 
        Thread t4 = new Thread(()->{
            for (int i = 0; i < 10; i++) {
                System.out.println(i);
            }
        });     
        t4.start();
    }
}

class MyThread extends Thread{
    public void run(){
        
        for (int i = 0; i < 10; i++) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            System.out.println(i);
        }
    }
}

class MyThread2 implements Runnable{
    public void run(){
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }
    }
}