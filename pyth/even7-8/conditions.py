
# conditionals:
# if, else , elif

# if condtion:

x = 30
y = 20

if True:
    print("Hello World")

if x > y :
    print(" X is greater than Y ")
else:
    print(" Y is greater than X ")

name = input("Enter Your Name : \n")
print(type(name))

if type(name) == str:
    print("Welcome  "+ name)
elif type(name) == int:
    print("Welcome  "+ str(name))
else:
    print("This is not a String and not a Number")




