#chance analytics
#random generators - numpy

import numpy as np
np.random.seed(123)
a = np.random.rand() #pseudo-random numbers
print(a)

#random but consistent ebtween runs

#coin toss
np.random.seed(123)
coin = np.random.randint(0, 2) #randomly generate 0 or 1
print(coin)
if coin == 0:
    print("heads")
else:
    print('tails')
    
#example:
'''
# NumPy is imported, seed is set
# Starting step
step = 50
# Roll the dice
dice = np.random.randint(1, 7)
# Finish the control construct
if dice <= 2 :
    step = step - 1
    print(dice, step)
elif dice >= 3 and dice <= 5 :
    step = step + 1
    print(dice, step)
else :
    step = step + np.random.randint(1,7)
    print (dice, step)

# Print out dice and step
'''

#random walk - path/random
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")

print(outcomes)

#tracking
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails)

#example
'''
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1] 

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

'''

#removing redundant line
'''
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1) #this was replaced from: step = step - 1
        #used to make sure that the max decrement would be 0, not giving negative values
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
'''

#using plotting with the data:
'''
# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
'''