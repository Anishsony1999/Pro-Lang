# def functino_name():

# def function_name(parameters):
# function is reusable block of code
# function can be called multiple times
# function can be used in multiple places

from typing import overload
from typing_extensions import override


def fan():
    print("Fan On")

fan() # function Call

def sum(a,b):
    return a+b

ans = sum(10,20)
print(ans)

# functions with default parameters

def add(a=20,b=20):
    return a+b

print(add(50,50))


# function call the same function this is called recursion

def print_num(n):
    if n > 10:
        return n
    print(n)
    return print_num(n+1)
    
print(print_num(1))


def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact(5))
# 5*4*3*2*1

def add_sum(x,y):
    return (x+y , x*y)

a,b = add_sum(3,3)
print(a,b) # 6 9

# [5,4,3,2,8,2,3,4,6] , target = 7
# output = [0,3]

# palindrome
# madam

# Malayalam
# a man, a plan, a canal: panama!

# function task , Bank Task

# 1,2,3 -> 1 login 2 create new account 3 exit

# login screen -> emil and password -> check -> if correct -> main menu
# main menu -> 1 balance 2 withdraw 3 deposit 4 exit

# creat new acc -> name , email, pass, confirm pass -> create acc

# 3,exit()

# oops
# 6 things
# class, object, inheritance, polymorphism, encapsulation, abstraction

# money, plan , thinks , place , workers 
# place , plan , workers , thinks -> home 

# place - memory
# plan - blue print
# workers - constuctor
# thinks - methods, variables
# Home - object

# class:
# class is the blue print of the object
# class is the collection of methods and variables

# object:
# object is the instance of the class
# object is the physical existence of the class

# class ClassName:
class Home:

    def __init__ (self,hall,kitchen,acc):
        self.name = "Home"
        self.acc = 0
        self.hall = hall
        self.kitchen = kitchen

    def __str__ (self):
        return f"Name : {self.name} Hall : {self.hall}"

    def sum(a,x,y):
        return x+y
    

# Object Creation
home1 = Home(2,1,1)
home2 = Home(3,2,1)
# home1.room = 2
# home1.hall = 1
# home1.kitchen = 1

# home2.room = 2
# home2.hall = 1
# home2.kitchen = 1

print("Home Class : ", home1) 

print(home1.kitchen)
# print(home1.sum(50,20))

str1 = list()

# constructor:
# constructor is the special method in the class
# constructor is used to initialize the variables
# constructor is called automatically when object is created
# constructor is used to allocate the memory - main point
# type of constructor:
# 1. default constructor - no parameters it will be called automatically when object is created
# 2. parameterized constructor - it will be called automatically when object is created with parameters


# pillers of oops:
# 1. inheritance
# 2. polymorphism
# 3. abstraction
# 4. encapsulation

# 1, inheritance:
    # inheritance is the onle way sharing 
    # sharing the properties of the parent class to the child class

    # Parent class -> super class , base class
    # Child class -> sub class, derived class , extended class

    # 5 types:
    # 1. single inheritance
    # 2. multiple inheritance
    # 3. multilevel inheritance
    # 4. hierarchical inheritance
    # 5. hybrid inheritance

# super() -> help to call near parent class methods, variables

# polymorphism:
    # poly - many
    # morph - forms
    # polymorphism - many forms

# 1. compile time polymorphism
    # method overloading
    # operator overloading
    # in python we can overload the methods because python is dynamic language ( interpreter)

# 2. run time polymorphism
    # method overriding


class Parent(object):

    def __init__(self):
        self.x = input("Enter Num 1 : \n")
        self.y = input("Enter Num 2 : \n")

    def add(self):
        return int(self.x) + int(self.y)

class Chile(Parent):

    @staticmethod
    def summ(x,y):
        return x+y

    @override
    def add(self):
        return int(self.x) * int(self.y)
        # return super().add() 

    def add_sum(self):
        return super().add()

def add():
    print("Add function called")

# abstraction:
    # abstraction is the process of hiding the implementation details from the user

# abstract class:
    # abstract class is the class which contains abstract methods

# abstract method:
    # abstract method is the method which is declared but not implemented(method with out body)
    # to implemnt abstract methosd u need to inherit the abstract class


from abc import ABC, abstractmethod

class Student(ABC):

    # id,name,class
    @abstractmethod
    def set_student_name(self,name):
        pass

    @abstractmethod
    def get_student_name(self):
        pass

    @abstractmethod
    def set_student_id(self,id):
        pass


class StudentImpl(Student):

    def set_student_name(self,name):
        self.name = name

    def get_student_name(self):
        return self.name

    def set_student_id(self,id):
        self.id = id

    def get_student_id(self):
        return self.id

student1 = StudentImpl()

student1.set_student_name("Anish")
student1.set_student_id(1)

print(student1.get_student_name())
