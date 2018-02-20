import numpy as np

l = [1, 2, 3, 4]
a = np.array([1, 2, 3])

# printing elements of list
for i in l:
    print(i)

# printing elements of numpy array
print
for e in a:
    print(e)

l.append(4)  # Append at end of list
# a.append(4) # Goves AttributeError

l = l + [5]  # added new element
# a = a + [5] # gives ValueError

# Vector Addition
# for element-wise Addition
l2 = []
for i in l:
    l2.append(i + i)
print(l)
# + sign with list does concatenation

print(a + a)  # Numpy array: does vector Addition

# scalar multiplication
print(2 * l)  # repeats the given list two times
print(2 * a)  # NumpyArray: multiply each element by 2

# Element wise sqauring of vector
# print(l ** 2)  # Gives TypeError
l2 = []
for e in l:
    l2.append(e * e)

print(a**2)  # With the numpy array

# for sqaureroot
print(np.sqrt(a))  # Element wise square root
print(np.log(a))  # Element wise log
print(np.exp(a))
print('===========')

# Dot Product
print("Dot Product.")
a = np.array([1, 2])
b = np.array([2, 1])
dot = 0
# By looping
for i, j in zip(a, b):
    dot += i * j
print("dot: {}".format(dot))
# print a * a # Gives element-wise multiplication

# ---- Different ways for dot product ------
# print np.sum(a * b)
# print (a * b).sum()
# print np.dot(a, b)
# print a.dot(b)
# print b.dot(a)

# Calculating the angle between the two vectors
amag = np.sqrt((a * a).sum())
print("Amag: {}".format(amag))
# OR
print("Amag: {}".format(amag).format(np.linalg.norm(a)))

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("cosangle: {}".format(cosangle))
angle = np.arccos(cosangle)
print("Actual angle: {}".format(angle))
print()
print('=============')

M = np.array([[1, 2], [3, 4]])
L = [[1, 2], [3, 4]]
# print L[0][0]
# print M[0, 0]
# Or
print(M[0, 0])

M2 = np.matrix([[1, 2], [3, 4]])  # Looks Similar but advice is against using it
# print M2
A = np.array(M2)  # Converting back to np.array
# print A

print(A.T)  # For matrix transpose

# Generating Matrices to work with
z = np.zeros(10)  # Creating an array of 10 zeros
z = np.zeros((10, 10))  # Creating an 10 x 10 zero matrix

O = np.ones((10, 10))  # Creating an 10 x 10 one matrix

# Creating 10 x 10 matrix of random numbers. Uniformly distributed numbers between 0 and 1
R = np.random.random((10, 10))

G = np.random.randn(10, 10)  # Gaussian distribution with mean 0 and variance 1
print(G.mean())
print(G.var())

# Matric Operations
A = np.array([[1, 2], [3, 4]])
Ainv = np.linalg.inv(A)
# print Ainv
# check if Inverse calculated properly
print(Ainv.dot(A))  # Gives identity matrix
# print A.dot(Ainv)

print(np.linalg.det(A))
print(np.diag(A))  # Gives the element on the diagonal of the matrix
print(np.diag([1, 2]))  # 1,2 in diagonal ,other place filled with 0

a = np.array([1, 2])
b = np.array([3, 4])
print(np.outer(a, b))  # Outer product
print(np.inner(a, b))  # Or np.dot(a, b)

# Matrix Trace: Sum of the diagonals of a matrix

print(np.trace(A))  # or np.diag(A).sum()

X = np.random.randn(100, 3)
covariance = np.cov(X)
print(covariance)

# Solve
# Ainv . A .x = b or x = Ainv.b
# A = np.array([[1,2], [3,4]])
# b = np.array([1,2])
# x = np.linalg.inv(A).dot(b)
# Or x = np.linalg.solve(A, b)
A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])
print(np.linalg.solve(A, b))
