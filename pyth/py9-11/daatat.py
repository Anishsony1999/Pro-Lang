
# tuple 
# tuple is immutable
# tuple is ordered

empty_tuple = ()
my_tuple = (5,"Anish",True,10.2)
tuple2 = tuple([2345,7,8,76,543])

(a,b,c,d) = my_tuple
(*i,j) = my_tuple
print(j) # 10.2

print(i) 
print(type(i))
print(type(my_tuple))

print(my_tuple.index("Anish")) 