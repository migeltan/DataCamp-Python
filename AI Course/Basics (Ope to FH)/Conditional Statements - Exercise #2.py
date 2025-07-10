#Conditional Statements on Python

"""
if, elif, else
Syntax: 
if - executes code if a condition is true
  
elif - executes code if the previous condition is false and this condition is true

else - executes code if all previous conditions are false
"""

#Example #1: Checking a condition

# num=-10

# if num>0:
#     print("The number is positive")
# elif num==0:
#     print("Number is zero")
# else:
#     print("Number is negative")
    
#Example #2: Nested Conditions

# age=25

# if age>18:
#     if age<30: #between 19 and 29
#         print("You are a young adult")
#     else:
#         print("You are an adult")    
        

"""
for Loops:
Syntax:

for item in sequence:
    Code block
    
    size = int(input("Enter number of elements: "))
numbers = []

for i in range(size):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("You entered:", numbers)


"""

#Example #1: Loops through a list

# fruits = ["Apple", "Banana", "Cherry"]

# for fruit in fruits:
#     print(fruit)
    
# #With range:

# for i in range(5):
#     print(i)
    
    
"""
while Loops:
Syntax:

while True:
    Code block

"""

#Example #1: Count down

# count=5

# while count>0:
#     print(count)
#     count -=1 #decrement
    
# print ("Outside we outsideeeeee cawdi")
    
"""
break and continue statements:
Syntax:

break:
for i in range(10):
    if i==5:
    break
    print(i)

continue:
for i in range(10):
    if i==7: #skips 7
        continue
    print(i)
    
"""

#Example #1: Using break

# for i in range(10):
#     if i==7:
#         continue
#     print(i)

# print ("We outsideeee cawdi") 

#Example #2

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
    
# print("We outsideeee cawdi")

""" 
Hands on Exercise
"""

#Exercise 1: Prime Number Checker
# num = int (input("Enter a number: "))

# if num>1:
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

#Exercise 2: Calculator

# def add (x, y):
#     return x+y

# def subtract (x,y):
#     return x-y

# def multiply (x, y):
#     return x*y

# def divide (x,y):
#     if  y != 0:
#         return x/y
#     else:
#         return "Not allowed to divide by zero"
    
# while True:
#     print("\nSelect:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
    
#     choice = input("Enter choice (1-5): ")
    
#     if choice == '5':
#         print("Exiting the calculator. Goodbye!")
#         break
    
#     num1=float(input("Enter first number: "))
#     num2=float(input("Enter second number: "))
    
#     if choice == '1':
#         print("Result: ", add(num1,num2))
#     elif choice == '2':
#         print("Result: ", subtract(num1,num2))
#     elif choice == '3':
#         print("Result: ", multiply(num1,num2))
#     elif choice == '4':
#         print("Result: ", divide(num1,num2))
#     else:
#         print("Invalid choice. Please try again.")
        
#Create a program to find largest number in a list using a for loop

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == numbers[0]:
        largest = num
    elif num > largest:
        largest = num

print ("The largest number is: ", largest)