#Assignment #3: Write a program to find power of a number using for loop.

print("Finds the power of the input:\n")
base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
ans = 1

#multiply 1 to base until exp is false
#so if 1 mult 3, and exp is 2 it will loop 2 more times
#ans will now be 3 mult to 3 again, then itll be 9, 2nd loop.
for i in range(exp):
    ans = ans * base

print(f"{base} to the power of {exp} is: {ans}")