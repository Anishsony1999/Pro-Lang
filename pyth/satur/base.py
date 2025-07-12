# programing 2 type type language
# 1, lowlevel language - 0101010
# 2, high level language - English


# highlevel language  to lowlwevel language - complier and interpreter

# complier vs interpreter
# complier - compile the entire code and generate the output
# interpreter - line by line translation of the code and generate the output

# python is a highlevel language
# python is a interpreted language

# python is a dynamically typed language
# python is a statically typed language


# variable
# variable is a name that is used to store a value
# variable is a reference to a value

# comments
# comments are used to explain the code
# interpreter will ignore the comments

# in python we must keep space 
# python is a case sensitive language


x = 10 # x is the name of the variable and 10 is the value
name = "Anish"

print(x) # 10
print(name) # Anish

# data types
# int, float, string, boolean:


x = 10 # x is integer data type
y = 10.5 # y is float data type
name = "Anish" # name is string data type 
is_true = False # is_true is boolean data type

# type() is used to check the data type of the variable

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(name)) # <class 'str'>
print(type(is_true)) # <class 'bool'>

# operators
# +, -, *, /, %, **, //

# print() # -> useing print function to print a new line or printing value in the same line
# type() # -> useing type function to check the data type of the variable
# input()  # -> useing input function to take input from the user


# name = input(" Enter Your Name: ")

# type casting
#--------------

x = "10"
print(type(x)) # <class 'str'>

x = int(x)
print(type(x)) # <class 'int'>

x = float(x)
print(type(x)) # <class 'float'>

x = 20

x = str(x)
print(type(x))

#x = int(name) # Error because name is a string data type and we can't convert string to integer

x = tuple()
x = (2.3,45,6)

x = (True,2,"anish",2) # tuple is immutable
print(x)

*i,j = x

print(i)

# x[0] = False # Error because tuple is immutable


# Set Data Type
# Set don't allow dublicate values
# Set is unordered

x = set()
x = {}

my_set = {1,"String",3.4,True}
my_set.add(10)
my_set.update([20,20,10])

my_set.remove(10)

new_set = my_set.copy()
new_set = set(my_set)

print(my_set)

bool_set = {True,False,1,0}

print(bool_set)


# [] -> list
# () -> tuple
# {} -> set

# Task

# [2,3,4,1,3,5,7,8] [6,4,2,33,2,11,2,3,4,56,7,8]
# 1, [2,3,4,7,8]
# 2, merge and sort without dublicate values 


# Dictionary
# dictionary is a collection of key value pairs
# dictionary dont allow dublicate keys but allow dublicate values

x = ["Anish",24,"Male"]
x[0] = "Anish Sony"

print(x)

# JSON -> JavaScript Object Notation

my_dict = {
    "name":"Anish",
    "age":24,
    "gender":"Anish",
    "name":"Anish Sony",
}
print(my_dict)
# add
my_dict["address"] = "KK"
# read
print(my_dict["name"]) # Anish
print(my_dict.get("name")) # Anish

# remove
# del my_dict["gender"]
my_dict.pop("gender")

# update
my_dict["name"] = "Anish Sony"


print(my_dict)

new_dict = dict()

print(my_dict.keys())
print(my_dict.values())

for key in my_dict:
    print(key,my_dict[key])

for key,val in my_dict.items():
    print(key,val)

print(my_dict.items()) # return list of tuples

user1 ={
    "name":"Anish",
    "age":24,
    "gender":"Male",
}

user2 ={
    "name": "Anusha",
    "age":24,
    "gender":"Female"
}

users ={
    "user1" : user1,
    "user2" : user2,
}

print(users["user2"]["name"])


x = ["Aish","Anisha","Anu"]

myNew_dic = dict()

for i in range(len(x)):
    myNew_dic[i] = x[i]

print(myNew_dic)

