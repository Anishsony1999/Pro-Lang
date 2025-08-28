

# String - data type

lname = 'Sony'
fname = str("Ani")

str
name = "anish sony1"

print(name[6])


# string function

print(name.title()) # Anish Sony
print(name.lstrip() + ".") # anish sony   .
print(name.rstrip() + ".") #    anish sony.
print(name.strip() + ".") # anish sony.
print(name.capitalize()) 
print(name.upper())
print(name.lower())

print(name.replace("anish","Binish"))

print(name) # anish sony

names = ['Ani','anu']
print('-'.join(names))

print(name.count('n'))
print(name.find('z'))
print(name[5].isalpha())
print(name[10].isdigit())


str1 = "main"

print("-1 : " + str1[-1]) 

print(str1[3])
str2 = str1 + " function"
print(len(str2))

print(str2[0 : 6])
print(str2[5:6])
print(str2[3 : 10])
print(str2[ 0 : -1])
print(str2[-3 :-1])

print(str2[ : -1])
print(str2[ 0 : ])
print(str2[ : ])
print(str2[ -1 : ])

print(str2[0 : : 3]) # mnutn
print(str2[-13 : -1 : 3]) # main function , mnut
print(str2[12 : 0 : -1])
print(str2[12 : 0 : -2])

str3  = "A man, a plan, a canal, Panama"
list1 = str3.split(" ")

print(list1)