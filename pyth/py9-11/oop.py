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

class Home:
    def __init__(self):
        print("constructor is called")

    def __init__(self,name):
        print(f"constructor is called {name}")

    def sum(self):
        print("sum is called")

# hom1 = Home()
hom2 = Home("Anish")
hom2.sum()
