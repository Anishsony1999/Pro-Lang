
set1 = set()
set2 = {"anish","ani","anime","ashik","anish"}

for i in set2:
    print(i)

set2.update(["Ani","Apple"])
set2.add("Mango")
set2.remove("ani")
name = set2.pop()
print(name)

set2.copy()

list1 = list(set2)
print(set2)
print(list1)


# 876 -> 678
# -12 -> -21