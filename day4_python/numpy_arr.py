import numpy as np

numbers =  np.array([1,2,3,4,5])

print(numbers )

#2D array
two_d = np.array([
    [2,4,5] , 
    [1,3,7]
    ])
print(two_d)

#3D array

three_D = np.array([
[ 
    [1,2] , [3,4]
    ],

[
    [5,6],[7,8]
    ]
    ])



print(three_D)

print(three_D.shape)
print(two_d.shape)
print(three_D.ndim)
print(two_d.ndim)
print(three_D.size)
print(two_d.size)
print(three_D.dtype)
print(two_d.dtype)

print(np.zeros((3,4)))
print(np.ones((3,4)))
print(np.arange(1,11))

#np.arange(start, stop, step)
print(np.arange(2,21,2))

#np.random.randint(low, high, size)
print(np.random.randint(1, 100, 5))