import csv

path = "C:/Users/HP/OneDrive/Desktop/Lang/pyth/py9-11/name.csv"

# with open(path,'r') as file :
#     data = csv.reader(file)
#     for row in data:
#         print(row)


# with open(path,mode='r') as file:

#     data = csv.DictReader(file)
#     for row in data:
#         print(row)

data = [["Names","Age","Adds"],["anish",24,"TVM"]]

with open('ani.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


data = [
    {"Ahe" : 24,"Add" :"TVM","Name":"Ani"}
]

with open('ANish.csv',mode='w',newline='') as file:
    header = ["Name","Ahe","Add"]
    writer = csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    