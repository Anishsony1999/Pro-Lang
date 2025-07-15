# diff ways of output
name = "Anish"
age = 24


string = "My name is " + name + " and I am " + str(age) + " years old."
string1 =  "My name is {} and I am {} years old.".format(name, age)
string2 = "My name is {0} and I am {1} years old.".format(name,age)
string3 = f"My name is {name} and I am {age} years old."

print(string1)
print(string2)
print(string3)
print(string)