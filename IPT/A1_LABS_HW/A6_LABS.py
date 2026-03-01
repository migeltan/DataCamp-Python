#Assignment #6: Write a program to find HCF (GCD) of two numbers. If and while
#highest common factor, greatest common divisor

print("This program finds the highest common factor (GCD) of two numbers.\n")
inp = int(input("Enter first number: "))
inp1 = int(input("Enter the second number: "))

if inp < inp1:
    smol = inp
else:
    smol = inp1
    
i = 1
hcf = 1

# fn = 6, sn = 3, smol = 3
# 1 <= 3
# 6 = 3, 2, 1 : 3 = 3, 1

while i <= smol:
    if inp % i == 0 and inp1 % i == 0:
        hcf = i #1 -> 3
    i += 1

print(f"\nThe highest common factor (GCD) is: {hcf}.")