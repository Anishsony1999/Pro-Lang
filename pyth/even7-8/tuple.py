# tuple Data type

# tuple is same as list but immutable

my_tuple = ()
my_tuple1 = tuple()
tuple1 = (True,10,5.5,"Anish")

print(type(my_tuple))
print(type(my_tuple1))

print(tuple1[3])
# tuple1[3] = "Anu"  # TypeError

print(tuple1.count("Anish"))
print(tuple1.index("Anish"))

num = (2,4,6,8)

list1 = list(num)
print(type(list1)) # tuple to list

u,v,w,x = num

u,*v,x = num 

print(v) # get a list of data
print(x)
