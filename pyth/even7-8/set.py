
# set data type

# set is a collection of data
# set dont allow duplicate valuess
# set is unordered

list1 = [2,2,3,5,9,7,9,0]

my_set = set()
my_set1 = {1,2,3}

list_set = set(list1)

print(type(my_set)) # <class 'set'>
print(type(my_set1)) # <class 'set'>

print(list_set) # {0, 2, 3, 5, 7, 9}

set1 = {True,"Anish","Anu","Ashliya",10,20.1,0,False}
print(set1) # {0, True, 'Anu', 'Ashliya', 'Anish', 20.1, 10}

set1 = {True,False,1,0,True,False}
print(set1) # {False, True}

x = list(set1)

print(type(x)) # <class 'list'>

set1.update([1,2,3,4,5,6])
print(set1) # {False, True, 2, 3, 4, 5, 6}

set1.remove(1)
print(set1)  # {False, 2, 3, 4, 5, 6}

print(set1.pop()) # remove and return

set1.add(10) # u can add a single data to the set
set1.clear() 

set2 = set1.copy()

