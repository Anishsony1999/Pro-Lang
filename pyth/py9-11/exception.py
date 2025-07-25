
# Exception Handling

# WHat is Exception ?
# Exception is an event which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
# In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error.

# Exception Types:

# 1. IndexError
# 2. NameError
# 3. ValueError
# 4. TypeError
# 5. ZeroDivisionError
# 6. FileNotFoundError


# input1= int(input("Enter a number: "))
# input2= int(input("Enter a number: "))

# try:
#     pass
# except:
#     pass
# finally:
#     pass

# try: 
#     print(input1/input2)

#     print(y)

# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# except Exception as e:
#     print(e)

# finally:
#     print("This is finally block")

# print("End of the program")

# try block:
#     # code block where exception can occur
# except block:
#     # code block where exception is handled

# finally block:
#     # code block whenever exception occurs or not



# raise is the keyword used to raise an exception

# name = input("Enter Your Name : ")

# if name.lower() == "anish":
#     raise Exception("Admin Not Allowed")


# creating custom exception

class UserNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


pasword = "123"
enterPass = "124"

try: 
    if pasword != enterPass:
        raise UserNotFoundError("User Not Found")
except UserNotFoundError as e:
    print(e)

