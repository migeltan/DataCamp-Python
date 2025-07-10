#Example #1

import pandas as pd

#Load dataset
df= pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#Explore structure
# print("First five rows: \n", df.head())

# print("Last 5 rows: \n", df.tail())

# print(df.info())
# print(df.describe())

#Example #2

selected_columns = df[["species", "sepal_length"]]
print("Selected Columns:\n", selected_columns)

filtered_rows = df [(df["sepal_length"]>5.0) & (df["species"] == "setosa")]
print(f"Filtered rows: {filtered_rows}")
