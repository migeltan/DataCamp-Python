#Filtering pandas Dataframe

import pandas as pd
import numpy as np
brics = pd.read_csv("C:/Users/Migel/OneDrive/Desktop/Python/ITPython DataCamp/brics.csv", index_col = 0)

#you can use comparison in dataframes like these
is_huge = brics['area'] > 8
print(brics)
print(brics[is_huge])

#you can also use bool ope
b = np.logical_and(brics['area']>8, brics['area']<10)
print(b)

#subset appropriately:
brics[np.logical_and(brics['area']>8, brics['area']<10)]
print(brics[np.logical_and(brics['area']>8, brics['area']<10)])

#example:
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Extract drives_right column as Series: dr
dr = cars['drives_right']
# Use dr to subset cars: sel
sel = [cars[dr]]
# Print sel
print(sel)
'''

#example of subsetting and converint to one liner
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Convert code to a one-linerw
sel = cars[cars['drives_right']] #subsets
# Print sel
print(sel)
'''

#example of comparison
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)
'''

#using logical ands
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
bet = np.logical_and(cpc > 100, cpc < 500)
medium = cars[bet]

# Print medium
print(medium)
'''