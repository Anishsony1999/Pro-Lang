
x = 10 / 0;

arr = [10, 20, 30];

try{
    document.writeln(arr[5]);
    document.writeln(x);

}catch(e){
    document.writeln("Exception : " + e);
}finally{
    document.writeln("Finally block");
}

// try block:
//     You can write code that may cause an exception.
// catch block:
//     You can handle the exception.
// finally block:
//     You can write code that will be executed after try and catch block.