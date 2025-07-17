
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


# string functions

name = "    anish sony    "

print(name.upper()) # ANISH SONY
print(name.lower()) # anish sony
print(name.capitalize()) # Anish sony
print(name.title()) # Anish Sony

print(name.strip()) # left and right space remove
print(name.lstrip() + " hi") # left space remove
print(name.rstrip() + " hi") # right space remove


print(name.find("i")) # 6
print(name.endswith("y"))  # False
print(name.startswith("a")) # Flase

print(name.replace("a", "A")) # Anish sony
print(name.replace("anish","Devika"))

list1 = name.split("i") # split method use to spilt string to list
print(list1)

# loops

# for loop
# while loop

# for loop

# for variable_name in sequence:
#     statement

# range function

# range(start, stop, step)

for i in range(10):
    print((i))

for i in range(5,10):
    print((i))

for i in range(5,10,2):
    print((i))

for i in range(10,1,-1):
    print(i)

for char in "Anish":
    if char == 'i':
        print( "this is i ")
    
# Anish -> hsinA

# While loop 

# variable initialization

# while condition:
#     statement
#     increment/decrement(iteration)

i = 10
while i > 0:
    print(i)
    i -= 1

while True: # this is an infinite loop
   print(i)
   i += 1
   break

# break 
# its help to break the current loop

for i in range(1,11):

    if i == 5 :
        break
    print(i)

# continue
# its help to skip the current iteration

for i in range(1,11):

    if i == 5 :
        continue
    print(i)

# pass
# pass is a placeholder for future code

name = "Devika"

if name == "Anish":
    pass

# Anish Sony -> hsinA ynoS
# Anish Sony -> ynoS hsinA
# palandrome -> Amma , Malayalam , 121 , Dad -> is a palandrome 

# inner loops

for i in range(1,11):
    for j in range(1,11):
        if i*j == 10:
            break
        print(i*j)
    print(" --------- ")


# input -> "String" -> count the vowels 

# Some more Data Types

# List
# Tuple
# Set
# Dictionary


