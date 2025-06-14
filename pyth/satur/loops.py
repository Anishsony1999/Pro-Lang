# loops
# ------

# while loop
# for loop


# while loop syntax

# variable = 0

# while condition:
#     print("condition is true")
#     itrations

x = 1

while x <= 10:
    if x == 5 :
        print("x is equal to 5")
    print(x)
    x = x + 1
else:
    print("x is greater than 10")


# for loop syntax

# for variable in range(start, stop, step):
#     print("condition is true")

for i in range(10):
    print(i)


# task :
    # print a even numbers from 1 to 100 / range(1,101)
    # take a input from the user like 2 then print a table

for i in range(100,0,-1):
    print(i)


# brake and continue 
# break -> break the loop
# continue -> skip the loop at the given condition is true

for i in range(1,10):

    if i == 5 :
        break
    print(i)


# get a age from the user 
# if age is less than 18 then print "you are not eligible to vote"
# if age is greater than 18 then print "you are eligible to vote"

# 0 - 12 -> child
# 13 - 19 -> teenager 
# 20 - 60 -> adult
# 61 - 100 -> senior citizon


list1 = ["Anish","Sangeetha","Bindu"]

for i in list1:
    print(i)



