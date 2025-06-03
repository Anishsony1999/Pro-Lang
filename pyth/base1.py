# If statement
x,y = 10,10
# Syntax:

# if condition: 
#     code block

if x > y :
    print("x is greater than y")

# If else statement

# Syntax:

# if condition:
#     code block 
# else:
#     code block

if x < y :
    print("x is less than y")
else :
    print("x is not less than y")

# If elif else statement

# Syntax:

# if condition:
#     code block
# elif condition:   
#     code block
# else:
#     code block


if x == y :
    print("x is equal to y")
elif x > y :
    print("x is greater than y")
else :
    print("x is less than y")

# Loops 
# Loops are used to repeat a block of code multiple times

# 1. For loop
# 2. While loop

# For loop
# Syntax:

# for variable in sequence:
#     code block

# Example:

# for (var i = 0; i < 10; i++) {
#     console.log(i);
# }


for i in range(10): # 0 - 9
    print(i)

print("----------------")
for i in range(1,11):
    print(i)

print("----------------")
for i in range(1,11,2):
    print(i)

print("----------------")
for i in range(10,0,-1):
    print(i,end=" ")

print("\n----------------")


name = "Anish"
for i in name:
    print(i)

arr = ['anish','kumar','manoj','noha','jebin']

for i in arr:
    print(i , end=",")

# inner for loop
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()


# Brake and continue statement
# Break
# Break is used to break the loop

# Example:

for i in range(10):
    if i == 5:
        break
    print(i) # 0 - 4

# Continue
# Continue is used to skip the current iteration

# Example:

for i in range(10):
    if i == 5:
        continue
    print(i) # 0 - 4,6 - 9
else:
    print("Loop is over")

#While loop

# Syntax:

# while condition:
#     code block

# Example:

i = 0
while i < 10:
    print(i)
    i += 1

# While else loop

# Syntax:

# while condition:
#     code block
# else:
#     code block

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("Loop is over")

# Break and continue statement

# Break

i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

# Continue

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

# infinite loop

while True:
    print("Hello")
    break

# Functions 
# Syntax:

# def function_name(parameters):
#     code block

# Example:

def add(x,y):
    print(x + y)

add(2,3)

# Function with return value

def add(x,y):
    return x + y

z = add(45,2)
print(z)

# Function with default parameter

def add(x,y=10):
    return x + y

z = add(45)
print(z)

x = int(input("Enter th enumber:  to add : "))
y = int(input("Enter th enumber:  to add : "))
z = add(x,y)
print(z)

# Recursion
# Function Call the same function again and again

x = int(input("Enter a num: "))
y = 10
def multi(y,x):
    if y == 0 :
        return
    multi(y-1,x)
    print(x , "*" , y , "=" , x*y)

multi(y,x)


# Built in functions
# len()
# max()
# min()
# sum()
# sorted()
# zip()
# map()
# filter()
# reduce() 

name = "Anish"
print(len(name))

for i in range(len(name)):
    print(name[i])

print("----------------")


x = 10
y = 20

z = max(x,y)

z = min(x,y)

z = sum([1,2,3,4,5]) # 15

z = sorted([56,24,46,231,53,6]) # [6,24, 46, 53, 56, 231]

print(z)


# filter()

chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vowels = ['a', 'e', 'i', 'o', 'u']

def filter_vowels(chr):
    if chr in vowels:
        return True
    else:
        return False

filtered_vowels = filter(filter_vowels, chr) # ['a', 'e', 'i']

print(list(filtered_vowels))

# *
# * *
# * * *
# * * * *
# * * * * *

#     *
#    * *
#   * * *
#  * * * *
# * * * * *