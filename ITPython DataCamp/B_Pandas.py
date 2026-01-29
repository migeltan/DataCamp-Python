#pandas, part 1 - brics and dataframe
#forming a tabular dataset
#row = observations
#column = varuable
#builds table from datasets
#uses panda if you want to create an array with different
#data sets since arrays are homogenous

#dataframe from dict
import pandas as pd
#keys (coltables) values (data, col by col)
dict = {
    'country':['Brazil', 'Russia', 'India', 'China', 'South Africa', 'Philippines'],
    'capital':['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria', 'Manila'],
    'area':[8.516, 17.10, 3.286, 9.597, 1.221, 2.221],
    'population':[200.4, 143.5, 1252, 1357, 52.98, 110]
}
#creates a dataframe from the dict above
brics = pd.DataFrame(dict)
#change index, instead of 0, 1, 2, itll be the equivalent:
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA', 'PH']
print(brics)
#inputs data from a file:
#since di mo naman iinput yung data manually it will be from a file
#csv - comma-separated values
#                                         paayos ng index
#brics1 = pd.read_csv("path/to/brics.csv", index_col=0)
#print(brics1)


#example
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# Import pandas as pd
import pandas as pd
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country':['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right':[True, False, False, False, True, True, True],
    'cars_per_cap':[809, 731, 588, 18, 200, 70, 45]
}
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
# Print cars
print(cars)


#example, incorrect rows index
# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
# Specify row labels of cars
cars.index = [(row_labels)]
# Print cars again
print(cars)
