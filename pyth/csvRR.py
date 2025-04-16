import csv

with open('test.csv',mode='w',newline='') as file:

    write = csv.writer(file)

    write.writerow(['name','age','add'])
    write.writerow(['Anish','24','tvm'])

# --------------- reading ----------------

with open('test.csv','r') as file:

    reader = csv.reader(file)

    for row in reader :
        print(row)

header = ['Name','Age','Add']
with open('test.csv',mode='w',newline='') as file:
     
    write = csv.DictWriter(file,fieldnames=header)

    write.writeheader()

    write.writerow({'Name':'Ani','Age':'23','Add':'TTVM'})
    write.writerow({'Name':'Ani','Age':'23','Add':'TTVM'})




