# loops :
# for loop, while loop, do while loop, for of loop, for in loop

# only two loop types
# for loop - used to iterate over a sequence - list tuple string etc
# while loop - used to iterate until a condition is true

# for loop syntax

# for variable in sequence:
#     statement(s)

# range() function - used to generate a sequence of numbers

line = "****************"


for i in range(11):
    print(i,end="")
else:
    print("")

print(line)

for i in range(1,11):
    print(i , end=",")
else:
    print("")

print(line)

for i in range(1,11,3):
    print(i, end=",")
else:
    print("")

# task - 10,9,8,7,6,5,4,3,2,1
# 1 to 100 -> 4 multiple also 7 divisible print

# while loop 

# varible declaration

# while condition:
#     statement(s)
#     increment/decrement

print(line)

i = 1

while i <= 10:
    print(i, end=",")
    i +=1
else:
    print(i)

# endless loop

# while True:
#     i +=1
#     print(i)

print(line)

for i in range(1,11):

    if i == 5:
        pass #continue # break
    print(i)

# break -> stops the loop
# continue -> skips the current iteration and continues with the next iteration
# pass  -> does nothing, used as a placeholder

i = 1

while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i +=1
else:
    print("loops End")


for i in range(1,3):
    for j in range(1,3):
        print(i,j)