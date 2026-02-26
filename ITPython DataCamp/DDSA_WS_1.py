#Pandas and Data Manipulation
import pandas as pd

df = pd.read_csv("C:/Users/Migel/OneDrive/Desktop/Python/ITPython DataCamp/brics.csv")
#df - dataframe 
# df.info(), df.type(), df.describe, etc.
# checks the info of the dataframe

#series:
# Creating a DataFrame from a dictionary
data = {'Name': ['Inday', 'Rock', 'Doging', 'NgobNgob'],
        'Age': [25, 30, 35, 40],
        'City': ['Confidential', 'Netherlands', 'Hague', 'Philippines']}
df = pd.DataFrame(data)
print(df)

#a file can be transformed
#csv to xscl to sql to json, etc.


#Functions:
df.head() #head of the data
df.sample(10) #10 rows/sample
#rows - axis 0, col - axis 1
df.info() #summary of dataframe
df.describe() #summary statistics

#Categorical distribution:
df['Gender'].unique() #shows the array
df['Gender'].nunique() #number
df['Gender'].value_counts() #count of gender

#Selecting and handling data
df['Name'] #single bracket for series, double for df