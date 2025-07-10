#Pythonic Code 

"""
1. Use descriptive variable names
2. Write modular code with functions and classes
3. Follow PEP 8 style guidelines
4. Leverage Python's predefined functions
"""

#List Comprehension
# [expression for item in iterable if condition]
#Create a list of squares
# squares = [x**2 for x in range(10)]
# print (squares)

#Filter even numbers
# even = [x for x in range(10) if x % 2 ==0]
# print(even)

#Lambda Functions
#Anonymous single expression functions defined using the lambda keyword
# lambda arguments: expression

add = lambda x, y: x+y
print (add(3,5))

"""
map() - applies a function to each item in an iterable
filter() - filters items based on a condtion
reduce() - reduces an iterable to a single value
"""

#map()
numbers = [1,2,3,4]
squares = map (lambda x: x**2, numbers) #squares each item at a time
print (list(squares))

#filter()
evenList = filter (lambda x: x%2 == 0, numbers)
print(list(evenList)) #filters based on the condition

#reduce()
from functools import reduce

numbers1 = [1,2,3,4]
product = reduce(lambda x, y: x * y, numbers)
print (product)

"""
os and sys modules
os modules- provides function to interact with the os
"""

# import os 
# print(os.getcwd())
# os.mkdir("test_dir")
# os.remove("fruits.txt")

# sys module
import sys 
print(sys.argv)
print(sys.version) #details abt python, etc.





