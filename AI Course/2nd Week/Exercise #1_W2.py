#Example #1

import numpy as np

# a = np.arange(1, 6)
# b = np.arange (6, 11)

# print("Add: ", a+b)
# print("Sub: ", a-b)
# print("Mul: ", a*b)
# print("Div: ", a/b)

#Example #2: 3x3 matrix

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]]) #ginawa lang 2d
print(f"Original Matrix: \n{matrix} \n")

#Transpose
transpose = matrix.T
print("Transpose: \n", transpose) #Switches columns and rows

another_matrix = np.array([[9,8,7], [6,5,4], [3,2,1]])
print("\nAddition: \n", matrix+another_matrix)
print("\nMultiplication: \n", matrix * another_matrix)