package main

import ("fmt")

func main(){
	// var name  string = "Anish"
	// var age = 24
	// last_name := "sony"
	// fmt.Println("name : "+name)
	// fmt.Println(age)
	// fmt.Println(last_name)
	var name string = "anish"
	var age = 24

	last_name := name
	fmt.Println(last_name)
	fmt.Println(age)

	print_name(name)
}


func print_name(name string ){
	fmt.Println(name)
}