
u = "Hello World"

ans =""

arr = u.split()

for i in arr:
    rev =" "
    for j in i:
        rev = j + rev
    ans += rev

print(ans)

list1 = [2,4,5,7,89,0,212,3,42,5]

count = 0

for i in range(len(list1)):
    if list1[i] %2 ==0 and list1[i] !=0 :
        count = count+1

print(count)

str = "Amma".lower()

i = 0
j = len(str)-1

while i < j :
    if str[i] != str[j] :
        print("its not a pali")
        break
    i +=1
    j -=1
else: 
    print("its a pali")