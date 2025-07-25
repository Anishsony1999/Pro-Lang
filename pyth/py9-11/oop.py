# oop -> object oriented programming
# what is oop?
# it is a way to write code in a way that is easy to understand and easy to maintain.
# because oops is realworld problem solving approach.

# 6 topics:

# 1. class
# 2. object
# 3. inheritance
# 4. polymorphism
# 5. encapsulation
# 6. abstraction

# we r building home what u need
# u need :
# place - memory 
# plan  - blueprint - class
# goods - variables - attributes
# workers - constructors 

# class - blueprint
# class is the blueprint of the object.
# class is a collection of variables and methods.
# class is a logical entity.
# class is a template.
# class is a user defined data type.

# sytax:
# class class_name:
#     variables
#     methods

# methods: -> functions inside class.


# object : -> real world entity.
# object is the instance of the class.
# object is a physical entity.

# varibale_name = class_name() # constructor


# class with constructor
# constructor is a special method.
# constructor is used to initialize the object.
# constructor is called automatically when object is created.
# constructor is called when object is created.
# constructor in python is __init__() method.

# constructor is help to allocate memory to the object.

# defalut constructor:
# it will be called automatically when object is created.




from typing import overload
from typing_extensions import override


class Home:
    def __init__(self):
        self.fan = False
        print("constructor is called")
    def  fan_on(self):
        self.fan = True
        print("fan is on")
    def fan_off(self):
        self.fan = False
        print("fan is off")
    def check(self):
        if self.fan == True:
            print("fan is on")
        else:
            print("fan is off")

hom1 = Home()
hom2 = Home()
hom1.check()
hom1.fan_on()
hom1.check()
hom1.fan_off()
hom1.check()
hom2.check()

# hom2 = Home("Anish")

# Inheritance:
# Inheritance is one Way sharing.
# Inheritance is a mechanism in which one class acquires the property of another class.

# 5 types of inheritance:
# 1. single inheritance
# 2. multiple inheritance -> one class inherits from multiple classes.
# 3. multilevel inheritance
# 4. hierarchical inheritance -> one class inherits from multiple classes.
# 5. hybrid inheritance

class Parent:

    def __init__(self,name):
        self.name = name
        self._age = 20
        self.__balance = 0

    def getName(self):

        print(f"Welcome {self.name}")
    
    def setBalance(self,balance):

        self.__balance = balance

parent = Parent("Anish")

parent.getName()

print(parent.__balance)

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self,name):
        pass

class Dog(Animal):

    def speak(self,name):
        print(f"{name} says bow bow")

class Cat(Animal):

    def speak(self,name):
        print(f"{name} says meow meow")

dog = Dog()
dog.speak("Tom")

cat = Cat()
cat.speak("Jerry")

