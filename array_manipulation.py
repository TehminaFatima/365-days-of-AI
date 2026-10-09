import numpy as np
# Create two arrays
array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[5, 6]])
 
# Concatenate vertically and horizontally
vertical_concat = np.concatenate((array_a, array_b), axis=0)
horizontal_concat = np.concatenate((array_a, array_b.T), axis=1)
 
print(vertical_concat)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
 
print(horizontal_concat)
# Output:
# [[1 2 5]
#  [3 4 6]]

unsorted_array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# Sort the array
sorted_array = np.sort(unsorted_array)
print(sorted_array)

unique_values, counts = np.unique(unsorted_array, return_counts=True)
print("Unique values: ", unique_values)

#filter the array using where
filtered_array = np.where(unsorted_array > 4)
print("Filtered array indices: ", filtered_array)

#flaten the 2d array
two_d_array = np.array([[1, 2, 3], [4,
    5, 6]])

flaten_array = two_d_array.flatten()
print("Flattened array: ", flaten_array)

ravel_array = two_d_array.ravel() # ravel() returns a flattened array, but it returns a view of the original array whenever possible. This means that if you modify the raveled array, it may also modify the original array. In contrast, flatten() always returns a copy of the data.
print("Raveled array: ", ravel_array)