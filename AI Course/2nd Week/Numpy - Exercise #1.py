#Numpy in Data Science
# Foundation library for numerical computations
# for large data sets

#Importing Numpy
import numpy as np

#Creating arrays
arr = np.array([1,2,3,4])
print(arr)

zeroes = np.zeros((3,3)) #2dimensional arrays #matrix
print(zeroes)

ones = np.ones ((2,4))
print(ones)

range_Array= np.arange(1,10,3) #spacing of the number furthest right
#ranging from first number to second, then spacing based on 3rd number
print(range_Array)

linspace_array = np.linspace(0,1,5) #evenly spaced number based on the 3rd num
print(linspace_array)

#Manipulating arrays
#arr = np.array([1,2,3,4,5,6]) #ginawa lang 2d
#reshaped = arr.reshape((2,3))
#print(reshaped)

#adding dimensions
arr = np.array ([1,2,3])
expanded = arr [:, np.newaxis]
print(expanded)

#Basic operations on array:

a=np.array([1,2,3])
b = np.array([4,5,6])

print(a+b) #Adds/mult/divides

# arr=np.array([4,16,25])
# print(np.sqrt(arr))
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))

#Array indexing, slicing, reshaping
#indexing
arr1 = np.array([10, 20, 30, 40, 50, 60])
print(arr1[2])
print(arr1[-1])

#slicing
print(arr[1:4])
print(arr[:3])

#reshaping
reshaped = arr.reshape (2,3)
print(reshaped)