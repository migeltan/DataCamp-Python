#looping data structures part1:

'''
syntax in dict:
for key, val in my_dict.items():

syntax in array:
for val in np.nditer (my_array):

'''

world = {'afghanistan': 30.55,
         'albania': 2.77,
         'algeria': 39.21}

#   a     b     are arbitrary variables
for key, value in world.items():
# a will be assigned to afghan, while b will be in flaot
    print(key + "--" + str(value))

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 63.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2
for val in bmi:
    print (val)

meas = np.array([np_height, np_weight])#using np
for val in np.nditer(meas): #use this function
    print(val) 

#example using a dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
# Iterate over europe
for key, val in europe.items():
    print ('the capital of ' + key + ' is ' + val )
    
#looping data structures part1:
#for pandas dataframe

import pandas as pd
brics = pd.read_csv("C:/Users/Migel/OneDrive/Desktop/Python/ITPython DataCamp/brics.csv", index_col = 0)
#to iterate what u want in pandas, you use iterrows()

'''
syntax:
for key, row in brics.iterrows():
print (key)
print(row)
'''
for label, row in brics.iterrows():
    print(label)
    print(row)

#subsetting
for label, row in brics.iterrows():
    print(label + ': ' +row['capital'])

#adding a column, counting the length of country name
for lab, row in brics.iterrows():
   #series on every ite
    brics.loc[lab, 'name_length'] = len(row['country'])
    
print(brics)

#using apply when adding a new column
brics['name_length'] = brics['country'].apply(len)
print(brics)

#example
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for a, row in cars.iterrows():
    print(a)
    print(row)
'''

#example
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ': ' + str(row['cars_per_cap']))

'''

#example
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
# Print cars
print(cars)
'''

#same pero using apply:
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)

cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)
'''