
# list

# What is list?
# List is a collection of items.(any type of data)
# List is a mutable.
# List is a ordered.
# List is a indexed.
# List is a iterable.

# list is same as String but String is immutable and list is mutable.

# empty list
my_list = []
# or
mylist = list()

my_list = [10,30.2,"Anish",True]
print(my_list[-1])


# slicing
print(my_list[1:2]) # 30.2
print(my_list[:]) # [10,30.2,"Anish",True]
print(my_list[::2]) # [10,"Anish"]
print(my_list[::-1]) # [True,"Anish",30.2,10]
print(my_list[1:]) # [30.2,"Anish",True]

my_list[1] = 20
print(my_list)

# list methods

# append -> method use to add element at the end of the list.
my_list.append("Sony")
my_list.append(100)

print(my_list)

# pop -> method use to remove element from the end of the list and return it.
x = my_list.pop()
print(x) # 100
my_list.pop(2)
print(my_list) # [10,20,True,"Sony"]


# insert -> method use to add element at the given index.
my_list.insert(2,"Anish")
print(my_list) # [10,20,"Anish",True,"Sony"]

# remove -> method use to remove element from the list.
my_list.remove("Anish")
print(my_list) # [10,20,True,"Sony"]

num_list = [4,56,342,2,3,3,24,64,7,86,8,534,2,242,2]

# sort -> method use to sort the list.
num_list.sort()
print(num_list) 

names = ["Anish","Anirudh","Devika","Reya","Suriya","zudio","Max"]
# names.sort()
# print(names)

# reverse -> method use to reverse the list.
# names.reverse()
# print(names)

names.sort(reverse=True)
print(names)

# clear -> method use to clear the list.
names.clear()
print(names)

# this is wrong way to copy list.

list1 = [1,2,3]
list2 = list1

print(list2[1])
list2[1] = 20
print(list2)

print(list1)

# using copy method

list1 = [1,2,3]
list2 = list1.copy()
list2[1] = 20
print(list1)
print(list2)

for i in list1:
    print(i)

# task
# [2,6,3,1,6,7,2,45,6,1,5] target = 7
# [1,3]
# [1,9]
