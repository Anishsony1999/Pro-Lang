
list1 = list()
list2 = []

print(type(list1))
print(type(list2))

names = ["Anish","Anna","Vishnu","ziyan","bindhu"]

print(len(names))

print(names[-3])

print(names[2])

print(names[0:2])
print(names[ 1 : : 2])
print("negathive : ", names[ : :-1])

for name in names:
    print(name)


names.append("Anusha") 
names.insert(0,"0")

names.remove("0")
del names[0]

name = names.pop(1) # return and remove

# names.sort()
# names.reverse()

names.sort(reverse=True)

print(name)
print(names)

# names.clear()

names2 = list(names)
# names2 = names.copy()
names2[1] = "Ani"
print(names2)
print(names)