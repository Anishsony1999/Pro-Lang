
dis1 = dict()
dit2 = {}

dict2 = {
    "Ani" : 35,
    "Anusha" :99,
    "Ani": 33
}
print("dupplicate : ", dict2)

dict2["Ani"] = 100
dict2["Ameen"] = 55

print(dict2)

print(dict2["Anusha"])
val = dict2.get("Ani")
print(val)

dict2.update({"Anusha":100})

for i in dict2.keys():
    print("key : ", i ," values : ",dict2[i])

print(dict2)

print(dict2.items())
print(dict2.popitem())

del dict2["Ani"]

print(dict2)

for i in dict2.items():
    print(i)



user1 ={
    "email" :"anish@123",
    "phone" : 975433
}

user2 ={
    "email" :"email@1234",
    "phone" : 9754333
}

users = {
    'user1' : user1,
    'user2' : user2
}

print(users["user1"]['email'])