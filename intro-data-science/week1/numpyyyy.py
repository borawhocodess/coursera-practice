import numpy as np
import math

np.set_printoptions(precision=2)

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

a = np.full((200, 200), 255)

print(a)

a = np.array([[1,2],[3,4],[5,6]])

b = np.array([a[0,0],a[1,1],a[2,1]])

print(b)
print(a[[0,1,2],[0,1,1]])
print(a>4)
print(a[a>4])

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

b = np.array([a[:2],a[:2,1:3],a[2,1]])

print(a)
print(b)

b[1][0][0] = 50 # WOWWWWWWWWW

print(a) # PASS BY REFERENCE WOOOOOOOOOW
print(b)

a = np.random.rand(10000,1000)
a = a * 10
print(a)
print(a[:,0])
print(a[:,0:1])
print(a[:,0:3])
print(a[:,[0,2,4]])
print(a[:,-1])
print(a[:,-1].mean())








#quiz

print("---------------------------------")

a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1, 4, 4)

print(a1, a1.shape, a1.ndim)
print(a2, a2.shape, a2.ndim)
print(a3, a3.shape, a3.ndim)
print(a4, a4.shape, a4.ndim)
print(a5, a5.shape, a5.ndim)