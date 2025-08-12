# Strings in Python 

# String is a sequence of characters.
# Strings are immutable.
# Strings are indexed.
# indexing starts from 0.

x = 'Hello World!'
y = str("Anish!")


print(len(y)) # 6
print(x[4]) # o
print(y[-1]) # y[len(y)-1]

#slicing

print(x[2 : 5]) # llo
print(x[2 : 10 ]) # llo Worl
print(x[4:4]) #
print(x[ 3 : ]) # lo World!
print(x[ :9]) # Hello Wor
print(x[-10 : -1]) # llo World
print(x [:]) # Hello World!
print(x[::-1]) # !dlroW olleH
print(x[2 : 10 : 2]) # loWr



# String Methods

x = "   Hello Ashliya   "
y = "."

print(x+y) #    Hello Ashliya   .
print(x.lstrip() + y) # Hello Ashliya   .
print(x.rstrip() + y) #    Hello Ashliya.
print(x.strip()+y) # Hello Ashliya.
print(x.upper()) #    HELLO ASHLIYA
print(x.lower()) #     hello ashliya
print(x.replace("Ashliya", "Anish")) #     Hello Anish

list1 = x.split('l')

print(list1) # ['   He', '', 'o Ash', 'iya   ']

print(x.find("A")) # 9
print(x[5].isalpha()) # True 
print(x[5].isdigit()) # False
print(x.startswith(" ")) # True
print(x.endswith("Ashliya")) # Flase

# 1, Hello World! -> !dlroW olleH
# 2, Hello Ashliya M Riyaz! -> olleH ayilhsA M !zayiR
# 3, Malayalam, dad ,{ a man, a plan, a canal: panama!}

# list Data Type
# ==============

# list is a collection of items in a particular order
# list also indexed
# list is similar to string but list is mutable
# list is a Container for store Data

list1 = [] # empty list
list2 = [1,2.2,"String",True]
list3 = list()

print(type(list1)) # <class 'list'>
print(list3)

print(list2[2]) # String
print(list2[:]) # [1,2.2,"String",True]
print(list2[ : 2]) #[1,2.2]

# mutable
list2[1] = 20

print(list2)

list4 = [5,3,5,3]

list5 = list2+list4


list2 += list4

print(list2)

# list methods

list2.insert(1,"insert data")

print(list2)

list2.append('adding data from the end')
print(list2)

x = list2.pop(1) # Remove and return item at index (default last).
print(x)
print(list2)

list2.remove(5)
print(list2)

num = [7,5,3,7,2,8,2,9,1,0,1]
# num.sort()
# print(num)

# num.reverse()
# print(num)

num.sort(reverse=True)
print(num)

num.extend([20,30,40])
print(num)

print(num.count(7))

num = [20,20,10,20]

num1 = num.copy() # way1
num1 = list(num) # way2
num1[0] =50

print(num) 
print(num1)

num.clear()
print(num)


fname="anish"
num = 9442016203
email = "anishsony@gmail.com"
website="anishsony1999.github.io/portfolio"

# out ="My name is "+fname+" my Number is "+ str(num)+" You Can mail me at "+email+" My site "+website
out = "My name is {} my Number is {} You Can mail me at {} My site {}".format(fname,num,email,website)
out = "My name is {0} my Number is {1} You Can mail me at {2} My site {3}".format(fname,num,email,website)
out = "My name is {name} my Number is {num} You Can mail me at {mail} My site {web}".format(
    name=fname,num=num,mail=email,web=website)
out = "My name is %s my Number is %d You Can mail me at %s My site %s"%(fname,num,email,website)

out = f"My name is {fname} my Number is {num} You Can mail me at {email} My site {website}"

print(type(out))
print(out)
