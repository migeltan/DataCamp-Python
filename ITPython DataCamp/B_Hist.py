#Histogram visualization
#Data distribution - uses bins and points, then uses bars for the heights
import matplotlib.pyplot as plt
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins = 3)

#Customizing plot
year = [1950, 1951, 1952, 1953, 1954, 1955, 2100] #random data
pop = [2.538, 2.57, 2.62, 2.77, 2.87, 3.12, 10.85] #random data



plt.plot(year, pop)

plt.xlabel('Year') #x axis labelling
plt.ylabel('Population') #yaxis labelling
plt.title('World Population Projections') #title on plot

plt.yticks([0, 2, 4, 6, 8, 10], #ranking
           ['0', '2B', '4B', '6B', '8B', '10B']) #billion of pop
plt.show()

#Plot is scattered and depends on the population
'''
# Import numpy as np
import numpy as np
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)
# Double np_pop
np_pop = np_pop * 2
# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)
# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
# Display the plot
plt.show()
'''

#plot is scattered and colored using c and alpha
'''
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()
'''

# Add grid() call
plt.grid(True)
plt.show()