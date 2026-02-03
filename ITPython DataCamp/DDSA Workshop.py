#variables, conditions, functions

#variables and data types
bakla = 20 #var, val
#must have meaningful variable types

#snake case, meaningn variables uses underscore
bakla_si_migel = 20
#case-sensitive ang python
#has no limit

#dates
from datetime import date, time, datetime
from collections import Counter
date = date.today()
time = time(1,30,0)
name= 'migel tan'

#formatted strings:
#parang printf with var at the end
print(f"Today is: {date}, time is: {time}, I'm a member of: {name}")

#concat
"hello" + "world"
#multi a string
hllo = "hello" * 3

#type casting
pi = "3.14"
pi = float(pi) #making it a float from string

#built-in functions
var = 324.1222
print(len(hllo))
print(round(var ,2)) #rounds to two
#print(min())
#print(max()) #max in a list 

#division
a = 9
b = 4
#print("Floor division", a // b) rounds fown
print ('Modulo: ', a % b)

'''
control flow basics - python conditionals
'''
'''
#if else syntax:
if condition:
    statement
elif condition:
    statement
else: #last na to
    statement
'''
#example:
age = 19
if age > 20:
    print(f"{age} is legal.")
else:
    print(f"{age} is not legal.")
    
#used comparison operators, refer to C_ComparisonOper
#used logical ope, refer to C_BooleanlOper

'''
#for loop syntax:
for variable in sequence:
    statement
'''
range = 1, 2,3,4,5,6,7,8, 9
for i in range:
    print (i)

'''
while-loop syntax:
while condition is true:
    statement
'''
i = 0
n = 3
while i< 3:
    print ("Thanks")
    i += 1

#zip function
names = ["Arthur", "Morgan", "Trevor", "Philips"]
ages = [25, 30, 35, 40]
cities = ["New York", "London", "Tokyo", "Los Angeles"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
    
#icebreaker
words = ['python', 'migel']
print(''.join(words))

'''
#functions
def function_name(parameters):
    #statement
    return expression

calling a function:
function_name(argument)
'''

price = 5.50
quantity = 10

#Function Header "def calculate_total(price, quantity)"
def calculate_total(price, quantity):
    total = price * quantity
    return total

#parameter and argument
#Parametemers "(price, quantity)"
def calculate_total(price, quantity):
    total = price * quantity
    return total
#actual na value na ipapasa from main function/other function
#Arguments "(5.50, 10)"
totalPrice = calculate_total(5.50, 10)
print(totalPrice)

#function without any parameter:
def print_pogi():
  for i in range:
        print("Hi Pogi!")
print_pogi()

#indexing and slicing:
#access starts by zero ofc
'''
syntax:
data = ['a', 'b', 'c']
data[0] prints a
data[-1] prints c

'''

#string slicing
string = 'MachineLearning'
first_word = string[0:7]
print(first_word)

#multiple indexing
readings = [10.2, 15.6, 12.1, 18.9, 9.8, 20.3]
even_index = readings [::2]
print(even_index)

#matrix indexing 
data_mat = ([101, 85, 20],
            [102, 92, 22],
            [103, 78, 21])

second_stud_data = data_mat[0][:]
second_stud_score = data_mat[1][:]
#appending to get 3rd col
#stud_age_data = data_mat[row[2] for row in data_mat]
stud_age_data = data_mat[2][:]
print (second_stud_data, second_stud_score, stud_age_data)


votes = ['yes', 'no', 'yes', 'yes', 'no', 'yes']
print(votes[1:3])
votes.pop(0) #pops the index
votes.remove("yes") #removes dynamically

#tuples - immutable, cannot be edited unlike lists
#uses parenthesis
coordinates = (19, 20.1, 33.1, 40.1)
print(coordinates[1])

#sets - unordered or unindexed mutable collections, not allowing duplicate values
#curly braces
roles = {'admin', 'editor', 'viewer', 'supervisor', 'programmer'}
print(roles) #unexpected printing
for role in roles:
    print (role)
    
#to see if it exists:
if "admin" in roles:
    print('admin exist') #if used in tuples and list, O^n 

#methods used in conversion
'''
list()
tuple()
set()
dict()

roles = list(roles) #changes it to the called function
'''

#pep8 - python enhancement proposal 8
#unified team style
#layouts:
'''
line length should have 79 characters max
indent should be at 4 spaces, not tabs
break line and align if a function has too many arguments


'''

