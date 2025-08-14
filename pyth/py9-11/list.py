
# List - > list
# list is a container of stored different type of data
# list is similar to String but list is mutable
# list is squance ordered
# list allow duplication of data

list1 = [True,10,10.5,"Hello"]
list2 = list("Anish")
print(list2)
print(type(list2))

# CRUD - create read update delete
new_list = [20,32,13,12,10]
new_list.append(10) # Append object to the end of the list.

print(new_list)

new_list.insert(1,1) # Insert object before index.

print(new_list)

x = new_list.pop() # Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range
print(x)

new_list.remove(10) # Remove first occurrence of value.
# Raises ValueError if the value is not present.

print(new_list)

new_list.clear()
print(new_list)

new_list += [2,2,2012,31,43,23,46,88,423,6] 

print(10 in new_list) # True or False

print(new_list[2]) # 30
print(new_list[ : ])

new_list[ 0 : 2 ] # [10,20]
new_list[ : : 2 ]

new_list[-2] # 60

new_list[0] = 100

print(new_list)

new_list.sort(reverse=True) 
# new_list.reverse()
print(new_list)

# target  = 20

# list = [1,2,3,3,5,10,20,10,22,8,18] ->  [5,7]

# Two dimention list

list1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(list1[2][2])

print(list1)

for i in list1:
    print(i)


list1  =  [1,2,3]
# list2 = list1

# print(list2)
# list2[0] = 100

list2 = list1.copy()
list2 = list(list1)

print(list2)

# [2,4,5,6]  [5,5,3,2,6] -> [2,3,4,5,6]

# Try to get new Achivement 