import numpy as np
arr = np.array([10,20,30,40])

print(arr[0])
print(arr[-1])

arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr[0])
print(arr[-1])
print(arr[1][2]) 

#slicing

arr = np.array([10,20,30,40,50])
print(arr[1:4]) 

#2D slicing
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr[0,:]) #print 1st row
print(arr[:,2]) #print 3rd column
print(arr[1: , 2:]) 
print(arr>5) # boolean indexing