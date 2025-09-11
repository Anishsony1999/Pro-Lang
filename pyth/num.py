
import numpy as np


arr = np.array([1,2,3,4,5])

print(arr * 2)

a=[1,2,3,4,5]
print(a * 2)

aa=[[1,2,3],[4,5,6]]
print(aa)
print(aa[1][1])

twod= np.array([[1,2,3],[4,5,6]])
print(twod[0][2])
print(twod)

print(twod.dtype)
print(twod.shape)
print(arr.shape)
print(twod.ndim)
print(arr.ndim)

list1 = []

# for i in range(1000):
#     list1.append(0)

arr2 = np.arange(0,11,2)
print(arr2)