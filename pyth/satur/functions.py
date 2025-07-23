# def functino_name():

# def function_name(parameters):
# function is reusable block of code
# function can be called multiple times
# function can be used in multiple places

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

    def __init__ (self,hall,kitchen):
        self.acc = 0
        self.hall = hall
        self.kitchen = kitchen

    def __str__ (self):
        return f"{self.room}"

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


