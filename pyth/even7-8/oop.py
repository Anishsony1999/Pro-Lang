

class Home:

    def __init__(self):
        self.fan = False

    def check(self):
        if self.fan :
            print("Fan is On")
        else:
            print("Fan is Off")

    def fan_on(self):
        self.fan = True
    
    def fan_off(self):
        self.fan = False

home1 = Home()
home1.fan_on()
home1.fan_off()
home1.check()


class Parent:

    def __init__(self):
        self.x = 10
    
    def add(self,x,y):
        return x+y
    
class Childe(Parent):
 
    def __init__(self):
        self.x =20
    
    def add(self,*args):
        return sum(args)
    
    def adding(self,x,y,z) -> int :
        return x+y+z

child  = Childe()

print(child.add(3,3,3))
print(child.adding(3,3,3))
print(child.x)


# Abstraction

from abc import ABC,abstractmethod

class Student(ABC):

    @abstractmethod
    def adding(self,x:int,y:int) -> int:
        pass

class StudentImp(Student):

    def adding(self,x:int,y:int):
        return x+y

student = StudentImp()
print(student.adding(3,3))



class __Bank:

    def __init__(self,name,email):
        self.name = name
        self._email = email
        self.__balance = 0

    def depo(self,amout):
        self.__balance += amout
    
    def withdrow(self,amout):
        self.__balance -= amout
    
    def balance(self):
        return self.__balance

user1 = __Bank("Anish","anishsony@gmail.com")

user1.depo(200)
user1.withdrow(100)
print(user1.balance())