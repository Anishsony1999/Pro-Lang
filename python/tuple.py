
# tuple

list1 = ["string",20,10.0,False]
list1[2] = 20

print(list1)

tuple1 = tuple() # list()
print(type(tuple1))

tuple2 = () # []
print(type(tuple2))

tuple3 = ("string",20,10.0,False)
# tuple3[2] = 20 bec immutable
print(tuple3)

print(tuple3.index(20))