import numpy as np

# 1D array
a = np.array([1, 2, 3])
print("1D:", a)

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D:\n", b)


# Create an array of 10 zeros
zeros = np.zeros(10)

# Create an array of 5 ones
ones = np.ones(5)

# Create an array of integers from 10 to 20
arr = np.arange(10, 21)

# Create an array of 5 evenly spaced numbers between 0 and 1
lin = np.linspace(0, 1, 5)

print("Zeros:", zeros)
print("Ones:", ones)
print("Range 10–20:", arr)
print("Linspace 0–1:", lin)


print(type(zeros))

a =np.array([1,2,3])
b = np.array([10,20,30])

print(a+b)

print("Sine:", np.sin(a))       # sin of each element
print("Square Root:", np.sqrt(b)) 
print("Exponent:", np.exp(a))   # e^x for each element
print("Log:", np.log(b))        # natural log


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# Element-wise multiplication
print("Element-wise:\n", x * y)

# Matrix multiplication
print("Dot product:\n", np.dot(x, y))  # OR x @ y
