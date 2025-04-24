package javalang;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;

public class FileHandling {
    // IO in java

    // 1) Byte Stream
    // 2) Character Stream

    // Byte Stream : 8 bit data
    // Character Stream : 16 bit data

    // Stream : flow of data

    // 1) Byte Stream : 8 bit data
    // FileInputStream ->  BufferInputStream 
    // FileOutputStream -> BufferOutputStream

    // 2) Character Stream : 16 bit data
    // FileReader -> BufferedReader
    // FileWriter -> BufferedWriter

   public static void main(String[] args) {
    
    try(FileReader fr = new FileReader("C:\\Users\\HP\\OneDrive\\Desktop\\Lang\\javalang\\text.txt");){
        int i;
        while((i=fr.read())!=-1){
            System.out.print((char)i);
        }
    }catch(Exception e){
        e.printStackTrace();
    }

   

   try(FileWriter fw = new FileWriter("C:\\Users\\HP\\OneDrive\\Desktop\\Lang\\javalang\\text.txt");){
    BufferedWriter bw = new BufferedWriter(fw);
    fw.write("Hello World");
   }catch(Exception e){
    e.printStackTrace();
   }

   }
   
}
