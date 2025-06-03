class Object{

    age;
    gender;
    name;

    set set_name(name){
        this.name=name;
    }
    get get_name(){
        return this.name;
    }
}

let obj1 = new Object();
obj1.set_name = "Anish";

document.writeln(obj1.get_name);