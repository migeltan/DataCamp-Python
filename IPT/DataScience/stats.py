# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Migel/Downloads/enhanced_student_habits_performance_dataset.csv")

# print(df.shape)        # (80000, 28) roughly
# print(df.dtypes)       # schema / data types
# print(df.isnull().sum()) # check for missing values
# print(df.describe())   # stats for numeric columns
# print(df.head())       # first 5 rows

sleep = df["sleep_hours"]
mean_sleep = sleep.mean()
std_sleep = sleep.std()

print("Mean Sleep Duration:", mean_sleep)
print("Standard Deviation:", std_sleep)
import matplotlib.pyplot as plt

plt.hist(sleep, bins=10)
plt.title("Histogram of Sleep Duration")
plt.xlabel("Hours of Sleep")
plt.ylabel("Frequency")

# Mean line
plt.axvline(mean_sleep, linestyle='dashed')

plt.show()
