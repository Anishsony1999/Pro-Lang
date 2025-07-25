
class Car:

    def __init__(self):
        self.base_speed = 10

    def get_speed(self):
        return self.base_speed

class BMW(Car):

    def __init__(self):
        super().__init__()
        self.speed = 60
    
    def get_speed(self):
        return self.speed

    def get_car_speed(self):
        # return super().get_speed()
        return self.base_speed

bmw = BMW()
print(bmw.get_car_speed())
print(bmw.get_speed())

# super() is used to call the parent class methods
# super() is used to call the parent class constructor
# super() is used to call the parent class attributes