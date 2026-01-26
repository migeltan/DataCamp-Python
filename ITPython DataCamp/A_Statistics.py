#stats: generation of data
#numpy has functions for data crunching such as:
#np.mean = ave
import numpy as np

'''
np_city = np.array([[1.64, 71.78],
                    [1.37, 63.35],
                    [1.6, 55.09],
                    [2.04, 74.85],
                    [2.04, 68.72]])
                    '''



#generate data - random made by numpy
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))

ave = np.mean(np_city[:, :])
print(ave)

#median - gitna
mid = np.median(np_city[:, :])
print(mid)

#correlation
cor = np.corrcoef(np_city[:, 0], np_city[:, 1])
print(cor)

#stdeviation
std = np.std(np_city[:, 0])
print(std)