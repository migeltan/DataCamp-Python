#Example #1 - Broadcasting Operations
import numpy as np
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# vector = np.array([1, 0, -1])

# result_add = matrix +vector
# print("Add: \n", result_add)

# result_mul = matrix *2
# print("Multiplication: \n", result_mul)

#Example #2 - Generate and filter a random dataset

#Generates random dataset
dataset = np.random.randint(1,51, size=(5,5))
print("Original: \n" , dataset)

#Filters values greater than 25 and replace with 0
dataset [dataset >25]=0
print("Modified Dataset: \n", dataset)

#Calculate summary stas]ts
print("Sum: ",np.sum (dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))
