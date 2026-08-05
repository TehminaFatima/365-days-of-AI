import numpy as np
arr = np.array([1,2,3,4])

print(arr+5)
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr+10)
arr = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([10,20,30])

print(arr+b)

a = np.array([[1],
              [2],
              [3]])

b = np.array([10,20,30])

print(a+b)

print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.sum())
print(arr.std())
print(arr.std())
