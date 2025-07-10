#Broadcasting in Numpy
# Broadcasting allows numpy to perform arithmetic operations
# on arrays of different shapes.
# Aligned from the right, matches the other array's dimension

import numpy as np

#array and scalar broadcasting
# arr = np.array([1,2,3])
# print(arr+10) #broadcasts to each array

# matrix = np.array ([[1,2,3], [4,5,6]])
# vector = np.array ([1, 0, 1])
# print (matrix + vector)

# #Aggregation functions 
# # Compute summary statistics for arrays
# arr = np.array([[1,2,3], [4,5,6]])

# print("Sum: ", np.sum(arr))
# print("Mean: ", np.mean(arr))
# print("Max: ", np.max(arr))
# print("Min: ", np.min(arr))
# print("STD: ", np.std (arr))
# print("Sum along rows: ", np.sum(arr, axis= 1))
# print("Sum along columns: ", np.sum(arr, axis=0))

#Boolean
# Filter elements from an array
arr = np.array([1,2,3,4,5,6])

evens = arr[arr %2==0]
print("Evens: ", evens)

arr[arr>3]=0
print ("Modified Array: ", arr)

np.random.seed(42)

#Random number generation and setting seeds.
# np.random 
random_Array = np.random.rand(3,3)
print("Random Array: \n", random_Array)

random_integers = np.random.randint(0,10, size = (2,3 ))
print("Random Integers: \n", random_integers)

