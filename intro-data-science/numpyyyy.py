import numpy as np
import math

a = np.array([[1,2,3],[4,5,6]])

print(a.shape)
print(a.ndim)
print(a.dtype)

a = np.zeros((2,3))
print(a)
a = np.ones((2,3))
print(a)
a = np.random.rand(2,3)
print(a)
a = np.arange(10, 50, 2)
print(a)
a = np.linspace(10, 50, 5)
print(a)

b = np.array([1,2,3,4,5])

c = a - b

d = a * b

print(c)
print(d)

twotimesa = a * 2

print(twotimesa)

print(twotimesa > 50)
print(twotimesa % 3 == 0)

a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])

print(a*b)
print(a@b)

print(b.sum())
print(b.min())
print(b.max())
print(b.mean())

b = np.arange(1,16,1).reshape(3,5)

print(b)