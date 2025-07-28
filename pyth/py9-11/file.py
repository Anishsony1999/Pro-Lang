
# file reading and writing in python

# 1, file reading  - open()


path = "C:/Users/HP/OneDrive/Desktop/Lang/pyth/test.txt"


try:
    file = open(path,"r")
    print(file.read())
    file.close()
except Exception as e:
    print(e)


with open(path,'r') as file:
    print(file.read())

