

# programing language in two types;


# 1. compiled language - convert into machine language - binary code
# 2. interpreted language - line by line execution

# compiler - c,c++,java
# interpreter - python, javascript, php, ruby, bash, shell

# python is interpreted language


# comments - single line - #
# multiline comments - ''' ''' or """ """


print("Hello World")

# ctrl + `

x = 10

# variable is a container which can store the data
# x is the variable and 10 is the value

print(x)

# data types 
'''
int - integer - 10,203,2003,20020
float - decimal - 23.4,43.2,432.23,3.14
string - " " or ' ' - "Anish","Hello World"
boolean - True or False 
'''

#type()
# type() is a function which returns the data type of the variable

print(type(x))

# int - Data Type

x = 10
print(type(x)) # int

x = 10.2
print(type(x)) # float

x = 'Anish'
print(type(x)) # str

x = True
print(type(x)) # bool

# input()
# input() is a function which takes input from the user using keyboard
# input() returns the input in string format

line1 = "*****************************"
line2 = " "
name = input("Enter Your Name : \n")

print(line1)
print(line2)
print("* welcome  : " + name + "     *")
print(line2)
print(line1)


x = input("Enter Any Number : \n") # str
y = input("Enter Any Number : \n") # str

# Type Conversion

x = int(x) # str to int
y = int(y) # str to int

z = x+y
print(z) # 20

print(type(z))

x = float(x) # int to float
print(type(x)) # float

x = str(x) # float to str
print(type(x)) # str

# oprators

# Arithmetic Operators

# + - * / % ** //

# Assignment Operators

# = += -= *= /= %= **= //=

# Comparison Operators

# == != > < >= <=

# Logical Operators

# and or not


