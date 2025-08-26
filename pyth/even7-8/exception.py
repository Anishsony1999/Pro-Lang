
try:        

    def div(x,y):
        return x / y

    x = div(
        int(input("Enter a Number : \n")),
        int(input("Enter a Num 2 : \n"))
    )

    print(f"The ans : {x}" if x is not None else "Enter Valide number")

    y = []

    print(y[2])

except ZeroDivisionError as e:
    print("Enter only Positive number")

except ValueError :
    print("Enter Proper Number")

except IndexError :
    print("wrong index")

except Exception as e:
    print(e)

finally:
    print("Finally block")

print("Program End")


[1,4,5,7,9,10]


