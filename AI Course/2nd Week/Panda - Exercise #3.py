#Panda - easy to use data structures
#Series - capable of holding data of any type
#DataFrame - 2 dimensional like a table

import pandas as pd 

#Holds data of anytype
s = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(s)

#Creates 2 dimensional table
data={"Name": ["Migel", "Mica"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)

#Data from CSV, Excel and other sources

#CSV File
df = pd.read_csv ("data.csv")
#Excel
df = pd.read_excel ("data.xlsx")

#Saving data to csv or excel
df.to_csv ("data.csv")#,index=False)
df.to_excel("data.xlsx")

#Viewing Data
print(df.head())
print(df.tail(3))
print(df.info())
print(df.describe())

#Selecting and Indexing
print(df[["Name", "Age"]])
print(df[df["Age"]>25])
print(df.iloc[0])
print(df.iloc[:, 0])
print(df.loc[:, "Name"])

