# labda functions;
    # syntax:
    # lambda arguments: expression

    # labda functions are anonymous functions.
    # labda functions are single line functions.
    # labda functions are used to create small functions
    # no need function name, keword , return statement.

from cProfile import label


def sum(a,b):
    return a+b

ans = sum(10,20) # 30

lambda a,b: a+b

print(lambda a,b: a+b) # <function <lambda> at 0x0000021213D33040>

print((lambda a,b: a+b)(10,20)) # 30

sum = lambda a,b: a+b
print(sum(10,20))

# map() -> map(function, iterable)

list1 = [1,2,3,4,5]

def power2(n):
    return n**2

list2 = []
for i in list1:
    list2.append(power2(i))


list3 = list(map(power2,list1))

# using lambda function

list4  = list(map(lambda n : n**2,list1))


print(list1)
print(list2)
print(list3)
print(list4)


# filter() -> filter(function, iterable)

list5 = list(filter( lambda n : n%2 == 0 , list1))

print(list5)

# sorted() -> sorted(iterable, key=function, reverse=True/False)

list6 = sorted(list1, key=lambda n : n%2 == 0, reverse=True)

data_list = [("Zayan",1),("Ginnu",2),("Anish",3)]

sorted_data = sorted(data_list, key= lambda n : n[0])
print(sorted_data)


# dir() -> dir(object)

for i in dir(dict):
    print(i)
