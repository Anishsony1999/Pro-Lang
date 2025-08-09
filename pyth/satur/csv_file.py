# csv - Comma Seprarated Values

import csv

# reading csv

file_path = "C:/Users/HP/OneDrive/Desktop/Lang/pyth/satur/users.csv"

# file = open(file_path,'r')
# reader  = csv.reader(file)

# for i in reader:
#     print(i)

# file.close()

# with open(file_path,'r') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# list1=[]

# with open(file_path,'r') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         if int(row['salary']) <= 25000:
#             list1.append(row)


# print(list1)


data = [
    ['Name','Age','City'],
    ['bhindhu',20,'TVM']
]

with open('name.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)


import pandas as pd

df = pd.read_csv(file_path)
print(df)