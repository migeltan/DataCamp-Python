#Functions

"""
Syntax:
def function_name(parameters):
    # code to execute
    return value  # optional
"""

#Example 1:

def add_numbers (x, y):
    return x+y

result = add_numbers(5, 3)
print("The sum is:", result)

#Scope and lifetime of variables:
#Local Variables:
"""
def outer_function():
    outer_var = "I am outside!"
    
    def inner_function():
        inner_var = "I am inside!"
        print(outer_var)  # Accessing outer variable
        print(inner_var)  # Accessing inner variable
    
    inner_function()
    # print(inner_var)  # This would raise an error, as inner_var is not accessible here
   
"""

# def greet():
#     message "Hello, world!"
#     print(message)
    
# greet()
#print(message)  # This would raise an error, as message is not accessible here

 
#Global variables:
"""
global_var = "I am global!"
def global_function():
    print(global_var)  # Accessing global variable
"""

greeting = "Hi"

def say_hello():
    print (greeting + " Migel!")

say_hello()
print (greeting + " Outside!")

#Example 2: Write a function to check if a number is even or odd
#and call it within another function



