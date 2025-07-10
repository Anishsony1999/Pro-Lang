
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

str = "Amma"
ans =""
for i in str:
    if i.isalpha():
        ans = ans + i
rev=""

for i in ans:
    rev = i + rev

if rev == ans : print("this is pali")
else : print("is not a pali")
