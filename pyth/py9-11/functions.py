

# global variable :
# we declare global variable in the top of the program
# we can access global variable in any function
# local variable :
# we declare local variable in the function
# we can access local variable in the function only

x = 0 # global variable

def add():
    global x
    x = 20 # local variable
    print(f'valuse of x ix {x}')

print(f'valuse of x ix {x}')


x = -123
ans = 0
sing = 1

def num_rev(x):
    if x < 0 :
        global sing
        sing = -1
        x = x * -1

    while x > 0 :

        y = x % 10

        x = x // 10

        print(y)
        global ans
        ans = ans * 10 + y

num_rev(x)

print(ans * sing)

# default parameters:

def sum(a:int=0,b:int=0):
    # print("before return",a+b)
    return a+b
    print("after return",a+b)

ans = sum(20,20)
print(ans)

a = 50
b = 50

print(sum(True,10))

# return function:

def retur_function():
    return add #  return a function

val = retur_function()

val()


def parent(name):
    name = name
    coin = 5
    time = 0
    def play():
        nonlocal coin
        nonlocal name
        nonlocal time

        time += 1
        coin -= 1

        print("times : ",time)
        print("blance Coin : " ,coin)
        print("name : ",name)
    return play

boy = parent("Anish") # 5
girl = parent("Anisha") # 5
boy()
girl()
boy()
boy()
boy()

# function call the same function is called recursion

def fac(num):
    if num == 1:
        return 1
    return num * fac(num-1)

print(fac(5))