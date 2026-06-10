#Assignment #5: Write a program to calculate factorial of a number. If and While

print("This program finds the factorial of your input.\n")
inp = int(input("Enter a number: "))
i = 1
res = 1

while i <= inp:
    if inp > 0:
#      i        i        i        i   i=4, then stop
# 4: 1x1 = 1, 1x2 = 2, 2x3 = 6, 6x4 = 24 
        res *= i #res * i
        print(res)
    i += 1
    
print(f"\nThe factorial of {inp} is {res}.")