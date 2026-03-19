#March 19, 2026
#Object-oriented programming

'''
return - is a special statement that you can use inside a function
or method to send the function's result back to the caller.

- return can be any python object, you can return numeric, or
sequence of objects (list, tuples, dicitonary)
'''
def get_even(numbers):
    return [num for num in numbers if not num % 2]

get_even([1, 2, 3, 4, 5, 6])

#Implicit Function
def add_one(x):
    result = x + 1
    #return result 

value = add_one(5)
print(value)

#New
return_value = print("Hello, World")
print(return_value)

#Multiple parameters
def add(a, b):
    result = a + b
    return result

print(add(2, 2))

#Statistics
import statistics as st

def describe(sample):
    return st.mean(sample), st.median(sample), st.mode(sample)

sample = [10, 2, 4, 7, 9, 3, 9, 8, 6, 7]
mean, median, mode = describe(sample)
print(describe(sample))

#Object-Oriented Programming
'''
Programming paradigm that provides a means of structuring
programs so that propertiees and behaviors are bundled
into individual objects.

Object can represent a student in this instance.
Each student should have a property and behavior.
properties - stud no, stud na, sub code, age, etc.
behavior - participate, engaged, recite, simulation, etc.

Classes and instances: Almost the same
classes - user-defined data structures. define functions called
methods. It is a blueprint for how something should be defined.

Instance - is an object that is built from aa class nd contains
real data.

Surname is a property of a class (person)
Tan is a Object/class name, Migel is a property
'''

#Defining a class: 
#class Keyword:
#   class body
        
#Instance Attributes - is specific to a particular instance
#of the class.

#Class Attributes
class Dog:
    #class attributes
    species = "Canis familiaris"
    
#constructor method
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
#instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
#another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Dog("Miles", 4) #Object
casper = Dog("Casper", 3) #object

print(miles.description())
print(miles.speak("aw aw"))

print(casper.speak("arf arf"))

'''
initialize object, then properties are inside init
then the methods are in the methods.
'''