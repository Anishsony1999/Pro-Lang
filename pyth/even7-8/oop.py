

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