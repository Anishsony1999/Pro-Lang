val = 10 # global variable

def cal():
    global val
    x = 10 # local variable
    val = val + 20 

cal()
cal()
print(val)


# closure

# def parent():
#     def child(x,y):
#         return x+y
    
#     return child

# a = parent()
# b = parent()
# c = parent()

# print(a("Anish ","Sony"))
# print(b(2,20))
# print(c(2.2,30.0))

# coin = 5
count = 0
def parent(name):
    coin = 5

    def play():
        global count
        nonlocal coin

        count +=1
        if coin < 1 :
            return "Your dont have coin"
        coin -= 1

        return f'{name } your balance is {coin}'
    return play

boy = parent("Anish")
girl = parent("Anisha")

print(boy())
print(girl())
print(boy())
print(boy())
print(boy())
print(girl())

print(count)