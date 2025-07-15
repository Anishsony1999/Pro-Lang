

def mul(num,x):
    
    if num==11:
        return
    print(num,"*",x,"=",num * x)
    return mul(num+1,x)



print(mul(1,5))
