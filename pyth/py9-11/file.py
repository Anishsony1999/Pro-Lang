
# # file reading and writing in python

# # 1, file reading  - open()


path = "C:/Users/HP/OneDrive/Desktop/Lang/pyth/test.txt"


# # try:
# #     file = open(path,"r")
# #     print(file.read())
# #     file.close()
# # except Exception as e:
# #     print(e)


# # r - read
# # w - write
# # rb - binary
# # wb - binary
# # a - append
# # r+ - read and write
# data = []

# with open(path,'r') as file:
#     data = file.read()
#     print(data)

# print("******************")

# with open(path,'r') as file:
#     line1 = file.readline()
#     line2 = file.readline()

#     print(line1,line2)

# with open(path,'r') as file:
#     data = file.readlines()
#     print(data)

# with open(path,'w') as file:
#     file.write("This is new String1")

# with open(path,'a') as file:
#     for i in data:

#         file.write(i)

users = dict()

with open(path,'r') as file:

    x = file.readlines()
    for i in x:
        user = i.split(":")
        users[user[0].strip()] = user[1].replace("\n","").strip()

print(users)

from datetime import date

date = date.today()

print(date)

# files handling

with open('text1.txt','w') as file:
    file.write("new line will append")
    


