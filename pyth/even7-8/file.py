
path ="text.txt"

try :

    with open(path,'w') as file:
        string = "Welcome Ashliya"
        file.writelines(string)

except FileNotFoundError:
    print("File Not Fount")

except Exception as e :
    print(e)