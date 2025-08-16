

try:
    list1 = []
    print(list1[4])

    open('text.txt')
    num1 = int(input("Enter a Number1 : \n "))
    num2 = int(input("Enter a Number2 : \n "))

    ans = num1/num2

    print(" Youe Ans : ",ans)

except ZeroDivisionError as e:
    print("Enter a positive number")

except ValueError :
    print("Enter a Integer ")

except FileNotFoundError :
    print("File Not Fount")

except Exception as e :
    print(e)

finally:
    print("Filally block")


print("Hello World")