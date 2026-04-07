
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv", index_col = 0)

yr = netflix_df[(netflix_df['type'] == 'Movie') & 
                           (netflix_df['release_year'] >= 1990) & 
                           (netflix_df['release_year'] < 2000)]

plt.hist(yr['duration'])
plt.show()

# Look at the plot and save the most frequent duration value
duration = 94

actmov = yr[yr['genre'] == 'Action']
short_movie_count = 0
for label, row in actmov.iterrows():
    if row['duration'] < 90:
        short_movie_count += 1