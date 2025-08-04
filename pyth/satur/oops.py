
class User:

    def __init__(self,name,email,phno,password):
        self.email = email
        self.name = name
        self._phno = phno 
        self.__password = password #declared as private variable
        self.balance = 0
    
    
    def getpaswd(self):
        return self.__password
    

    def check_user(self,name,pasw):
        if name == self.name and pasw == self.__password:
            return self.email


obj = User('Adi','bbi.dfy@gmail.com',9898799,'1234')
# print(obj.__password)

name = input("Enter the name : \n")
paswd = input("Enter u r pass : \n")

print(obj.check_user(name,paswd))


# create 3 user -> store in a list[]

# email,pass -> email,pass -> welcome User_name