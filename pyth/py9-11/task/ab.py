from abc import ABC,abstractmethod

class UserAbc(ABC):

    @abstractmethod
    def get_username(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def set_balance(self,balance):
        pass

    @abstractmethod
    def get_email(self):
        pass

    @abstractmethod
    def set_email(self,email):
        pass

    @abstractmethod
    def get_password(self):
        pass

class User(UserAbc):

    def __init__(self,name,email,password):
        self.name = name
        self.__password = password
        self.email = email
        self.__balance = 0

    def get_username(self):
        return self.name

    def get_balance(self):
        return self.__balance

    def set_balance(self,balance):
        self.__balance += balance

    def get_email(self):
        return self.email

    def set_email(self,email):
        self.email = email

    def get_password(self):
        return self.__password
    
    def __str__(self):
        return f" {self.name}"
    

class Transatction(ABC):

    @abstractmethod
    def check_password(users,password):
        pass

    @abstractmethod
    def create_new_user(name,email,password):
        pass

    @abstractmethod
    def deposite(user,balance):
        pass

    @abstractmethod
    def withdrow(user,balance):
        pass

class Bank(Transatction):


    def check_password(self,users:list[User],password:str):

        for user in users:
            if user.get_password() == password :
                return user     

    def create_new_user(self,name,email,password):
        return User(name,email,password)

    def deposite(self,user,balance):
        user.set_balance(user.get_balance()+balance)
        return user.get_balance()

    def withdrow(self,user,balance):
        bal = user.get_balance()

        if bal > balance:
            bal -= balance
            user.set_balance(bal)
            return user.get_balance()
        else :
            raise Exception("Blanace illa Monna")
        
