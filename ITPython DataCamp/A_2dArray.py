#2 dimensional arrays

import numpy as np
np_height = np.array([1.72, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79 ],
                 [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d)

#shape 2 r 5 c
print(np_2d.shape)

#subsetting a 2d array
#           r  c
print(np_2d[0][2]) #prints index that matrix
print(np_2d[0, 2]) #same func

#           rc r c
print(np_2d[:, 1:3]) #blank trans to 0
print(np_2d[1:, :]) #weight 1:0
print(np_2d[:1, :]) #height

#example
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)
# Print out the 50th row of np_baseball
print(np_baseball[49: ])
# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
# Print out height of 124th player
print(np_baseball[1:0 , :123])

# Print out addition of np_baseball and updated
#print(np_baseball + updated)
# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])
# Print out product of np_baseball and conversion
print (np_baseball * conversion)

