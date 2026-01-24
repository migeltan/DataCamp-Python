#packages - directory of python script
#script = modules, specify functions, methods, etc.
#import numpy as np, matplotlib, pandas, etc.

import numpy as np
#from numpy input array

print(np.version)
np.array([1, 2, 3])

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
fam_ext = fam + ['me', 1.79]
print(str(len(fam_ext)) + " elements in fam_ext")
np_fam = np.array(fam_ext)

'''
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)
# Print out np_height_in
print(np_height_in)
# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254
# Print np_height_m
print(np_height_m)
'''

#mathlib, uses pi for that
#from math import pi
import math as mp

# Calculate C
C = 2 * 0.43 * mp.pi
# Calculate A
A = mp.pi * 0.43 ** 2
print("Circumference: " + str(C))
print("Area: " + str(A))

add = np.array([True, 1, 2]) + np.array([3, 4, False])
print(add)

'''
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print (np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print (np_height_in[100:111])
'''