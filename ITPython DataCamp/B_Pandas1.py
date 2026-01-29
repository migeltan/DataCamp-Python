#pandas, part 2 - index and select data
#square brackets, loc and iloc
#selects specific column/row
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

#Selecting a specific column/row
brics1= brics[['country', 'capital']]
print(brics1)

#You can also slice
brics1 = brics[1:4]
print(brics1)

#loc - label based
#col access is through quootes inside square brackets
#row access is through slicing
print(brics.loc['RU'])
print(brics.loc[['RU']]) #AS A DATAFRAME
print(brics.loc[['RU', 'IN', 'CH']])
print(brics.loc[['RU', 'IN', 'CH'], ['country', 'capital']]) #prints only these
print(brics.loc[:,['country', 'capital']]) #end to end slice

#iloc - int position based
#rather than calling strings, u can call through index
print(brics.iloc[[1]]) #row access
print(brics.iloc[[1,2,3]]) 
print(brics.iloc[[1,2,3],[0,1]]) #row and col access
print(brics.iloc[:, [0,1]])#end to end slice

#example
'''
# Import cars data
cars = pd.read_csv('cars.csv', index_col = 0)
# Print out country column as Pandas Series
print(cars['country'])
# Print out country column as Pandas DataFrame
print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])
'''

#slicing
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Print out drives_right value of Morocco
print(cars)
print(cars.iloc[[5], [2]])
# Print sub-DataFrame
print(cars.iloc[[4,5], [1,2]])
'''

#slicing
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out drives_right column as Series
print(cars.iloc[:, 2])
# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])
# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:, [0, 2]])
'''