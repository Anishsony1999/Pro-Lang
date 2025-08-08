# function function_name(parameters){}
# def function_name(parameters):
    # pass

def sum(x,y):
    
    return x+y


# x = sum(10,20)
# print(x)

def numbers(x):
    if x == 0:
        return
    print(x)
    numbers(x-1)
    print(x)

numbers(10)


def fac(x):
    if x == 1:
        return 1
    
    return x * fac(x-1)

print(fac(5))


x = False
x = bool(x)
print(x)

if(True == 1):
    print("True")


x = 5 + 3j

print(x.imag)
print(x.real)
print(type(x))

# ['Anish','anish','ashliya','Ashliya','Greeshmaa','greeshma'] 
# -> ['Anish','ashliya','Greeshmaa','greeshma']

# [ {,[,(,),],} ] -> true
# [ {,},(,),[,] ] -> true
# [ {,(,},),[,] ] -> false

coin = 10 # global variable

def parent(name):
    coin = 5 # local
    def play():
        nonlocal coin
        coin -= 1

        print(name,"Avilable balance : ",coin)
    
    return play

boy = parent("Anish")
girl = parent("Ashliya")


boy()
girl()
boy()
boy()



# def function_name():

# we no need def, no need function name

add = lambda x,y : x+y # (x,y) -> x+y

print(add(20,20))


def power(n):
    return n**2


powers = lambda x : x**2

print(powers(2))
print(power(2))


def sqr(n):
    return n**2 

nums = [2,3,4,5,1]

for i in range(len(nums)):
    nums[i] = sqr(nums[i])

print(nums)

nums = list(map(lambda x : x**2,nums))
print(nums)