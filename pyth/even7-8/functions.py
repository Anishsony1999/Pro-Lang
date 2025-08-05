# function function_name(parameters){}
# def function_name(parameters):


# def sum(x=0,y=0):
    
#     return x+y


# x = sum(10,20)
# print(x)

def numbers(x):
    if x == 0:
        return
 
    numbers(x-1)
    print(x)

numbers(10)
