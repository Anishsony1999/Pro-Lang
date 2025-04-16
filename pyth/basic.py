
def play_game():
    balance = 10
    def play():
        nonlocal balance
        balance -= 1
        print(f'avilable balance{balance}')
    return play

ani = play_game()

ani()

def sqr(num):return num * num
print(sqr(2))

sqts = lambda num : num * num
print(sqts(2))

def add_two(num):return num + 2

add_two_num = lambda num : num + 2

print(add_two_num(10))

def add(num1,num2):
    return num1 + num2

adding = lambda num1,num2 : num1 + num2

print(adding(10,20))

def fun2():
    x = 10
    return lambda num : num + x

y = fun2()
# y = lambda x : x + 10

print(y(10))

#######################

def fuc1(x):
    return lambda num :  num + x

ans = fuc1(10) # x
ans1 = fuc1(25)

print(ans(20)) # num
print(ans1(25))

####################


numbers = [ 3,5,7,8,10,12]

sqr  = map(lambda num : num * num,numbers)

print(list(sqr))

###############

odd_num  = filter(lambda num : num % 2 !=0 ,numbers)
print(list(odd_num))

# for i in numbers:
#     if i % 2 !=0 :
#         print(i)

from functools import reduce

adding_nums = reduce(lambda add , crr : add + crr, numbers)

def adding_count():
    count = 0
    for i in numbers:
        count += i
    
    print(count) #45


# print(adding_nums)

print(sum(numbers))
adding_count()




x = 10101010 # -> 0  XOR
y = 745379563 # ->  1
# ======================

x = 54
y = 12

# y = 54
# x = 12

# =================

x = 5 ^ 6 ^ 6 ^ 5 ^ 1 

print(x)

x = 468
y = x % 10 # 8
z = int( x /10 )  # 46
ans  = y * 10 # 80

y = "745379563"

ans = 0
for i in y :
    ans ^= int(i) #11

print(ans)

# OOP 

# 1) Class 
# 2) Object

# =======================================


class Home:

    def __init__(self,room,color,lights):
        self.room = room
        self.color = color
        self.lights = lights
        self.name = "Sweet Home"

    def lightOn(self):
        print(f"{self.lights} light will be on")

    def lightOff(self):
        print(f"{self.lights} light will be off")

    # def __str__(self):
    #     return self.name


vismaya = Home(3,'Rose','white')
print(vismaya)

shilpa = Home(3,'White','white')

vismaya.lightOn()
shilpa.lightOn()


class Car:

    def __init__(self):
        self.engine = 'BMW'
        self.tyre = 'MRF'

class Tesla(Car):

    def __init__(self):
        super().__init__()
        self.power = 'electric'



    
