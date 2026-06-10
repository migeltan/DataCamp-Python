#Assignment #7: Write a program to find the lowest common multiple of two numbers. If and while
print("This program will find the LCM of two numbers: \n")

inp = int(input("Enter the first number: "))
inp1 = int(input("Enter the second number: "))

if inp > inp1:
    high = inp
else:
    high = inp1

lcm = high

while True:
    if lcm % inp == 0 and lcm % inp1 == 0:
        break
    lcm += high
    
print(f"\nThe Lowest Common Multiple is {lcm}.")
