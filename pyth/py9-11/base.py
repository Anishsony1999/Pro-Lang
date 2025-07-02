# loops

# 1, while loop
# 2, for loop

# while condition:
    # python code

x = 1

while x < 10:
    print(x ,"Hello World")
    print(x)
    x = x + 1
else:
    print(x)

# for loop


# for variable in range(start, end, step):
#     py code



for i in range(10):
    print(i)

print("-----------------")

for i in range(11,21):
    print(i)

print("-----------------")

for i in range(0,11,2):
    print(i)

print("-----------------")

for i in range(10,0,-1):
    print(i)
else:
    print("loops End")


# nested loops

for i in range(1,6): 
    for j in range(1,4): 
        print(i,j) 

    print("1st Loop " + str(i))

else:
    print("All loops are End")

# break and continue statement

for i in range(1,11):

    if i == 5:
        continue # break
    print(i)

while True:
    print("End loop")
    break


for i in "Anish":
    print(i,end=" ")

    