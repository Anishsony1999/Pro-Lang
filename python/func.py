
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

# def table(x):

#     for i in range(1,11):
#         print(i , " * ",x," = ", i*x)

#     print("*" * 15)

# x = table
# print(type(x))
# x(10)


# def parent():

#     def add(x,y):
#         return x+y
    
#     return add

# x = parent()

# print(x(10,20))


# recursive

# def print_name(name):
#     print(name)

# def greeting(name : str):
#     welcome = f"Welcome {name}"
#     print_name(welcome)

# greeting("Anish")

def nums(x):
    if x == 11:
        return
    print(x)
    nums(x+1)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(3))

# 3 * 2 * 1
# 5 * 4* 3 *2 *1