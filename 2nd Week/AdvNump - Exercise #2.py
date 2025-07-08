#Broadcasting in Numpy
# Broadcasting allows numpy to perform arithmetic operations
# on arrays of different shapes.
# Aligned from the right, matches the other array's dimension

import numpy as np

#array and scalar broadcasting
arr = np.array([1,2,3])
print(arr+10) #broadcasts to each array

matrix = np.array ([[1,2,3], [4,5,6]])
vector = np.array ([1, 0, 1])
print (matrix + vector)

#Aggregation functions 
# Compute summary statistics for arrays
arr = np.array([[1,2,3], [4,5,6]])

print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("STD: ", np.std (arr))
print("Sum along rows: ", np.sum(arr, axis= 1))
print("Sum along columns: ", np.sum(arr, axis=0))

#Boolean