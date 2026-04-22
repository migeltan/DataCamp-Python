#PROBLEM 1
userinp = []
for i in range(5):
    inp = int(input("Enter 5 numbers: "))
    userinp.append(inp)

def sumOfList(inp):
    sumlist = sum(inp)
    print(f"Sum of this list is: {sumlist}")

def largestNumber(inp):
    largest = max(inp)
    print(f"Largest number is: {largest}")

sumOfList(userinp)
largestNumber(userinp)

#PROBLEM 2
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist.append("orange")
mytuple = tuple(mylist)
print(mytuple)

#PROBLEM 3
mydict = {
    "name" : "Migel Tan",
    "age" : "20",
    "course" : "BSIT"
}

keysprint = mydict.keys()
print(keysprint)

valuesprint = mydict.values()
print(valuesprint)

print(mydict.items())

#PROBLEM 4
num = 4

def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
        
print(is_even(num))
    
#PROBLEM 5
import math

try:
    inp = int(input("Enter a number: "))
    square = math.sqrt(inp)
except:
    print("No square root for this integer!")
else:
    print(f"Square root is: {square}")
finally:
    print("done program")
    