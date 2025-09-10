
# function dec
# def add():
#     num1 = int(input("Enter a number!"))
#     num2 = int(input("Enter a number!"))
#     print(num1 + num2)

# def add(x ,y, z = 10):

#     ans = x + y + z
#     return ans


# num1 = int(input("Enter a number!"))
# num2 = int(input("Enter a number!"))

# x = add(num1,num2,20)
# print(x)

def table(x):

    for i in range(1,11):
        print(i , " * ",x," = ", i*x)

    print("*" * 15)

x = table
print(type(x))
x(10)
