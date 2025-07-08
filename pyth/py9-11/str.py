
task = """

*
* *
* * *
* * * *
* * * * *


    *  
   * *
  * * *
 * * * *
* * * * *


"""

# String -> str
# String is a sequence of characters
# String is immutable ->  can't change

string = "Hello World"
string1 = str("Hello World")

if string == string1:
   print("Equal")

print(len(string)) # 11 
print(type(string)) # < class 'str'>

char = 'A'

print(ord(char)) # char to ascii

name = "Anish"
name = name + " " + "Sony"

# indexing  - index number is starting from 0

print(name[6]) # A

# slicing
print(name[:]) # Anish Sony
print(name[2:5]) # ish
print(name[ :5]) # Anish
print(name[2:]) # ish Sony

print(name[ : :2]) # AihSn

print(name[-10]) # A
print(name[::-1])

print(name[-10 : -1])

s1 = "    Hello   World   "
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

print(s1.upper())
print(s1)
print(s1.lower())

print(s1.replace("World","Anish"))
print(s1.split("World"))
print(s1.endswith("World"))
print(s1.startswith(" "))
print(s1.find("W"))
print(s1[5].isalpha())
print(s1.join(["Anish","Sony"]))

# Malayalam 
# A man, a plan, a canal -- Panama!

# input - Hello World !
# 1, ! dlroW olleH
# 2, olleH dlorW !

# List - > list
# list is a container of stored different type of data
# list is similar to String but list is mutable
# list is squance ordered
# list allow duplication of data

list1 = [True,10,10.5,"Hello"]
list2 = list("Anish")
print(list2)
print(type(list2))

# CRUD - create read update delete
new_list = [20,32,13,12,10]
new_list.append(10)

print(new_list)

