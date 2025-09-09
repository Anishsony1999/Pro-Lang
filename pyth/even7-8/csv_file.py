import csv

file_path = "C:/Users/HP/OneDrive/Desktop/Lang/pyth/satur/users.csv"



with open(file_path,'r') as file:
    reader = csv.reader(file)

    # print(reader)
    for row in reader:
        print(row)


with open(file_path,'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row) 