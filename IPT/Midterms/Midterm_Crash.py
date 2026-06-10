if (11>8):
    print("hello")
    print("hi")

msg =\
    "'is this message correct?'"

name = "migel"
print(name[:3])

#enter your age
print ("enter age")
age = int(input("Enter your age: "))
if (age<18):
    print("illegal")
else:
    ("fine")
    
#assignment
x, y= "in x", "in y"
print(x, y)
#will print in x in y

x, y = y, x
print(x, y)
#will print in y in x

#string format
age = 20
txt = "My name is Migel and I am {} year's old"
print (txt.format(age))
#will print "My name is Migel and I am 20 year's old"

txt2 = "my name is migel and i am " + str(age) + "year's old"
print(txt2)
#will print the same

#string f
name = f"My name is migel, i am {age} year's old" 

#string w speci
order1 = "chicken"
order2 = "spaghetti"
pay = 25

myorder = "I want {2} with {1} and I'll be paying {0} dollars."
print(myorder.format(pay, order1, order2))
#will print "I want spaghetti with chicken and I'll be paryinh 25 dollars"

#escape chars
esc = "I am\\ my mothers\n child, and \t i love myself,\b no matter what."
print(esc)

#print without space
print("a", "b", "c", sep = ' ')
print("migelhtan", "pup.edu.ph", sep="@iskolarngbayan.")
print("Hello ladies and ", end = ' ')
print("gentlemen!")

#stores inside this variable
name = input("Enter your name: ")
#converts string to int
age = int(input("Enter your age: "))
print(f"Your name is {name} and you are {age} year's old.")
#will print according to input

#shorthand if else

age = 18
print("legal age") if age>=18 else print("not legal")

age = 25
if (age>18):
    print("above or equal to 18")
    if(age>=18 and age<20):
        print("cannot drink alc but an adult")
    else:
        print("can drink alcohol")
        
        
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i<6:
    print(i)
    i+= 1
else:
    print("is no longer less than 6")
    
for x in range (6):
    if x == 3:
        break
    print(x)
#equivalent to printing 2-30 by 3, so 2+3 = 2, 5, 8..

x = [0,1,2,3,4,5,6,7,8,9,10,11]
print(x[2:11])

fruits = ["saging", "mangga", "mansanas"]
for x in fruits:
    print(x)
    if x == "mangga":
        break
    
#list example:
fruits = ["saging", "mangga", "mansanas"]
newlist = [] #creates a newlist para sa gusto natin makita
for x in fruits:
    newlist.append(x.upper()) #capitalizes all chars in the list
    
#comprehension
newlist = [x.upper() for x in fruits] #capitalizes all chars in the list
print(newlist)

#conditioning
newlist = [x for x in fruits if x != "saging"]
print(newlist)

import filecmp

x = [1, 2, 3, 4, 5]
y = [3, 4, 5]
print(max(x))

x = [1, 2, 3, 4, 5]
x.append(6)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thisset = {"apple", "banana", "cherry"}
# #prints a specific value
# for x in thisset:
#     print(x)
        
#checks if its in the set
# print ("banana" in thisset)
thisset.add("mango")
print(thisset)

thisdict = {
    "brand" : "louis vuitton",
    "model" : "wallet",
    "year" : 2025
}

x = thisdict.items()
print(x)

#list and dict using zip()
keys = ["name", "age", "course"]
values = ["Migel", 19, "BSIT"]
result = dict(zip(keys, values))
print(result)

try:
    print("hello")
    # a wrong statement
except:
    print("sumn wrong")
else:
    print("nun wrong")
finally:
    print("end")
    
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 0:
    raise Exception("This is incorrect!")

#try
try:
    x = int(input("Enter a number: "))
    result = 10 / x

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result is:", result)

finally:
    print("This always runs.")
    
    
def print_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    print("Hello,", name)

print_name("Migel")   # works
print_name(str(123))       # error

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Migel", age=19, course="BSIT")

def sum_two_args (x, y):
    return print(x + y)
sum_two_args(10, 20)

from math import ceil
#lambda
print(abs(-123))
print(ceil(1.2425))


#==== OOP ====
# CLASS: Blueprint for creating objects
class Animal:
    
    # CLASS VARIABLE: Shared by all instances of the class
    kingdom = "Animalia"
    
    # CONSTRUCTOR (used for INSTANTIATION)
    def __init__(self, name, age):
        # INSTANCE VARIABLES (data unique to each object)
        self.name = name
        self.age = age
    
    # METHOD: A function inside a class
    def speak(self):
        return "Some generic animal sound"

class Cat(Animal):
    def __init__ (self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = age
        self.color = color
        
    def speak(self):
        return "Meow!"
    
    def owner(self):
        return f"owned by migel tan"
    
# INHERITANCE: Dog class inherits from Animal
class Dog(Animal):
    
    # CONSTRUCTOR (calls parent constructor using super())
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed  # additional INSTANCE VARIABLE
    
    # METHOD OVERRIDING (part of inheritance, replaces parent method)
    def speak(self):
        return "Woof!"
    
    # FUNCTION OVERLOADING (Python style using default arguments)
    def info(self, extra=None):
        if extra:
            return f"{self.name} is a {self.breed} and {extra}"
        return f"{self.name} is a {self.breed}"
    
    # OPERATOR OVERLOADING: Overloading + operator
    def __add__(self, other):
        return self.age + other.age  # combines ages of two dogs


# INSTANTIATION: Creating objects from class
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "Labrador")
cat1 = Cat("Cream", 2, "Calico", "Brown, White, Black")

# OBJECT / INSTANCE: dog1 and dog2 are instances of Dog class

# ACCESSING DATA MEMBERS (instance variables)
print(dog1.name)   # Buddy
print(dog1.age)    # 3

# ACCESSING CLASS VARIABLE
print(dog1.kingdom)  # Animalia

# CALLING METHODS
print(dog1.speak())  # Woof!

# FUNCTION OVERLOADING DEMO
print(dog1.info())  
print(dog1.info("very playful"))

# OPERATOR OVERLOADING DEMO
print(dog1 + dog2)  # adds ages: 3 + 5 = 8

print(cat1.color)

