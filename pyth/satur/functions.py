# def functino_name():

# def function_name(parameters):
# function is reusable block of code
# function can be called multiple times
# function can be used in multiple places

def fan():
    print("Fan On")

fan() # function Call

def sum(a,b):
    return a+b

ans = sum(10,20)
print(ans)

# functions with default parameters

def add(a=20,b=20):
    return a+b

print(add(50,50))


# function call the same function this is called recursion

def print_num(n):
    if n > 10:
        return n
    print(n)
    return print_num(n+1)
    
print(print_num(1))


def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact(5))
# 5*4*3*2*1

def add_sum(x,y):
    return (x+y , x*y)

a,b = add_sum(3,3)
print(a,b) # 6 9

# [5,4,3,2,8,2,3,4,6] , target = 7
# output = [0,3]

# palindrome
# madam

# Malayalam
# a man, a plan, a canal: panama!

# function task , Bank Task

# 1,2,3 -> 1 login 2 create new account 3 exit

# login screen -> emil and password -> check -> if correct -> main menu
# main menu -> 1 balance 2 withdraw 3 deposit 4 exit

# creat new acc -> name , email, pass, confirm pass -> create acc

# 3,exit()