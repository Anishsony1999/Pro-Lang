
# Dictionary
# dictionary is a collection of key value pairs
# dictionary dont allow dublicate keys but allow dublicate values 
# don't allow nulls

my_dict = dict()
my_dict1 = {}

print(type(my_dict))
print(type(my_dict1))

list1 = [1,'Anish','TVM']
list1[1] = 'Ashliya'
list1.insert(3,'?')
print(list1)


user = {'no':1,'name':'Anish','add':'TVM'}

user1 = dict(name='anish',age=24,add='TVM')

# add

user1['add'] = 'Tvm'

# reading
print(user1['age']) # 24
print(user1.get('age')) #24

# update 
user1['age'] = 21
user1.update({'age':25})

# del
# del user1['age']
x = user1.pop('age')

print(x) # 21
print(user1) 

print(user1.keys()) # returen all Keys # dict_keys(['name', 'add'])
print(user1.values()) # return all values # dict_values(['anish', 'Tvm'])

for i,j in user1.items(): # list of tuple
    print(i,j)

user1['name'] = 'Ashliya'

print(user1['name'])

user1 ={
    'name' :'Anish',
    'age' : 24
}

user2 = {
    'name' : 'Ashliya',
    'age' : 21
}

users = {
    'user1': user1,
    'user2' : user2
}

print(users)