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

zeros_array = np.zeros((3,4)) # this will create a 3x4 array filled with zeros
print(zeros_array) 

arrange_array = np.arange(0,10,2) #It will create an array of numbers from 0 to 10 with a step of 2
print(arrange_array) 

linspace_aray = np.linspace( 0 , 1,5) # it will create an array of 5 evenly spaced numbers between 0 and 1
print(linspace_aray)

reshaped_array = two_d.reshape(3,2) # it will reshape the 2D array into a 3x2 array
print(reshaped_array)

array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[5, 6]])
concatenated_array = np.concatenate((array_a, array_b), axis=0)
print("Concatenated Array:\n", concatenated_array) # concatenated array concatenates array_a and array_b along the first axis (rows)
 
# Stacking
stacked_array = np.vstack((array_a, array_b))  # Vertical stacking
print("Stacked Array:\n", stacked_array) # stacked array will be same as concatenated array