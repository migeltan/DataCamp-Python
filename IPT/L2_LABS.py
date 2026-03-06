#function

#def function_name(parameters):
    #statements
    #return expression

#function prototype/decla: user-defined
#1st part of function: return data type
#def

#2nd part: function_name
#3rd part: function parameter

# def function_name (formal parameter);
#function heading
#function definition
#int name(actual parameter)
#function body
#{ statement }

#function call
#parameter passing: formal -> actual parameter
#function statement
#function return

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

#1. Default Argumentsg
'''A default argument is a parameter that assumes a 
default value if a value is not provided in the function call for 
that argument.'''
def myFun(x, y=50):
    print("\nx: ", x)
    print("y: ", y)

myFun(10)

#2. Keyword Arguments
''' In keyword arguments, values are passed by explicitly 
specifying the parameter names, so the order doesn't matter. '''
def student(fname, lname):
    print(fname, lname)

student(fname='\nGeeks', lname='Practice')
student(lname='Practice', fname='Geeks')

#3. Positional Value
''' In positional arguments, values are assigned to parameters 
based on their order in the function call. '''
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("\nCase-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

#4. Arbitrary Arguments
''' In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a 
variable number of arguments to a function using special symbols. 
There are two special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments) '''
def myFun(*args, **kwargs):
    print("\nNon-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

#Functions within Functions
''' A function defined inside another function is called an inner function (or nested function). 
It can access variables from the enclosing function's scope and is often used to keep logic protected and organized. '''
def f1():
    s = '\nI love Migel Tan'
    def f2():
        print(s)
        
    f2()
f1()
