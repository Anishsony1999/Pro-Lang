
# oprators in python 
# +,-,*,/,%     
# ** , //

# = is assignment operator
# == is comparision operator
# != is not qual to operator


# >, <, >=, <= 
# and, or, not


# conditional statement
# if, else, elif

# if condition:
#     py code

if 10 > 5:
    print("10 is greater than 5")
print("hello world")

# if else condition

if 10 < 5 :
    pass
else:
    print("10 is less than 5")

x = 10 

if x > 5:
    print("x is greater than 5")
elif x == 5 : 
    print("x is equal to 5")
else:
    print("x is less than 5")


# input() -> takes input from user, by default input is string

name = input("Enter Your Name: ")

line1 = "***************"
line2 = " Welcome " + name  # concatenation

print(line1)
print(line2)
print(line1)

# typeCasting
# one type to another type

x = input("Enter Any Number :\n")

if type(x) == str :
    # type casting -> str to int
    num = int(x)
    print(num + 10)

num = float(x)
print(type(num)) # float 10.0
print(num + 10)

num = bool("False")
print(num)

x = str(10) 


# if condition:
    # if condition:

    # else:

x = 20

if x > 5:
    if x > 7 :
        print("x is greater than 7")
        if x > 10 :
            print("x is greater than 10")
        elif x == 10 :
            print("x is equal to 10")
        else:
            print("x is less than 10")
    else:
        print("x is less than 7")
else:
    print("x is less than 5")

