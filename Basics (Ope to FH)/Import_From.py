# Importing modules in Python
# Similar to headers in C, modules in Python allow you to organize 
# your code into separate files. This makes it easier to manage 
# and reuse code across different projects.

#Module
# import math
# print (math.sqrt(16))

# #Import a particular function
# from math import sqrt
# print(sqrt(16))

# #Renaming imports
# import math as m
# print(m.sqrt(16))

# #Custom Modules

# #Exercise 1: Factorials

# def factorial (n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# def print_factorial(n):
#     result = factorial(n)
#     print("\n")
#     print (f"The factorial of {n} is: {result}")

# print_factorial(5)

#Exercise 2: Module, math
# import math

def add(a,b):
    return a+b

def subtract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    if b!=0:
        return a/b
    else:
        return "Division not allowed"