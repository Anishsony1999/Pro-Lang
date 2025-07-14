
# variables

x = 4 
y = 4.4
name = "Anish"
is_bool = True 

print(type(is_bool))

# Conditions 

# if condition 

# Syntax 
# if condition:

x = 10
y = 15

if True :
    print("Printing Because Condition is True")

# if x > y :
#     print(" x is greater than y ")

# if x < y :
#     print(" x is less than y")


# if else condition
x =10
y =20
if x > y :
    print(" x is greater than y ")
else :
    print(" x is less than y")

# if elif condition

x = 10
y = 10

if x > y :
    print(" x is greater than y ")
elif x == y :
    print(" x is equal to y ")
else :
    print(" x is less than y")

# type casting
num = "24" # string
num = int(num) # string to int

x = 10
y = int("10") # string to int

print(type(y))

x = 10
x = str(x) # int to string

bol = True
bol = str(bol) # bool to string

print(type(bol))

float_num = 24.4
float_num = int(float_num) # float to int

print(float_num)

# and or not

x = 11 
y = 20

if x > 10 and y > 10 :
    print("Both are greater than 10")

if x > 10 or y > 10 :
    print("Atleast one is greater than 10")

if not x > 10 :
    print("x is not greater than 10")


# String Methods

# String is a squence of characters
# String is immutable
# String is index based

# String index start with 0

name = "Anish Sony"

print(name[7])
print(len(name))

print(name[-10])

# slicing
print(name[0 : 5]) # Anish
print(name [  : ]) # Anish Sony
print(name[ 0 : 10 ]) # Anish Sony
print(name[0 : 10 : 2]) # AihSn

print(name[-10 : -1])

print(name[::-1]) # reverse string