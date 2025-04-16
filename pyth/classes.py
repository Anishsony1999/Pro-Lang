class Bank:

    def __init__(self,name,email = None):
        self.__name = name
        if email == None:
            self.__email = None
        else:
            self.__email = email
    
    # def set_name(self,name):
    #     self.__name = name

    def print_name(self):
        print(self.__name)
    def get_email(self):
        print(self.__email)
class Child:
    def __init__(self):
        pass

