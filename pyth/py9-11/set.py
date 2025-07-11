
# set Data Type
# set is a collection of data
# set dont allow duplicate valuess
# set is unordered

# sytax:
from tkinter import N


my_set = {2,4,5,"Anish",(1,2,3),True,2.2}
print(type(my_set))
print(my_set)

set1 = {}
set2 = set([3,4,6,7,8])

print(set2)

# add element in set 

my_set.add(2)
print(my_set)

# remove element from set

my_set.remove(2)
print(my_set)

copy_set = my_set.copy()
copy_set = set(my_set)


set1 ={1,2,3,4}
set2 ={3,4,5,6}

# union
new_set = set1.union(set2)
print(new_set)

# update

set1.update(set2)
print(set1)

# Task:
# [2,3,4,4,6,8,3,18,2,54,54]

# 12 -> 21
# -12 -> -21


# [1,2,3,4,5,6] [4,5,6,7,8]


# dictionary

# dictionary dont allow duplicate keys
# dictionary is key value pair
# dictionary is ordered

# syntax:

my_dict = {
    "name":"Anish",
    "age":20,
    "roll":123,
}

print(type(my_dict))

# my_dict = dict()

user = ["Anish",20,123]
print(user[0]) # "Anish"

print(my_dict["name"])

# add element in dictionary

my_dict["gender"] = "male"
print(my_dict)
# remove element from dictionary

my_dict.pop("gender") # remove element by key
print(my_dict)

del my_dict["age"] # remove element by key

# update element in dictionary

my_dict["name"] = "Anish Sony"
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) # data type -> dist_items -> list of tuples

for key,value in my_dict.items():
    print(key,value)


user1 ={
    "name":"anish",
    "age":24,
}

user2 ={
    "name":"anusha",
    "age":24,
}

users = {
    "user1":user1,
    "user2":user2,
}

print(users)