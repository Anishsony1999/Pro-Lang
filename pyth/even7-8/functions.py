# function function_name(parameters){}
# def function_name(parameters):
    # pass

def sum(x=0,y=0):
    
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