
    
def sqr(n):
    return n**2

list1 = [3,5,7,3,2,5,10]
ans = list()

for i in list1:
    ans.append(sqr(i))

# print(ans)


# lambda function 
# def add(x,y): return x+y
# lambda args : expression
a = lambda x,y : x+y



# filter()
even = list(filter(lambda x : x%2 == 0,list1))


# map()
list1 = list(map(lambda x : x**2 ,list1))


# sorted()

words =['Apple','ben','mango']
sorted_list = sorted(words,key=lambda word : len(word))


def main():
    print(even)
    print(sorted_list)
    print(a(2,2))
    print('File name of lambda : ',__name__)
    print(list1)

if __name__ == '__main__':
    main()