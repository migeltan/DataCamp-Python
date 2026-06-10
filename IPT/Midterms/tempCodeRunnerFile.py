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