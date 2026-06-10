#Assignment #4: Write a program to find all the factors of a number. If and While

print("This program finds the factors of a number.\n")
inp = int(input("Enter a number: "))
i = 1
print(f"Factors of {inp} are: ")

while i <= inp:
    if inp % i == 0:
        print (i)
    i += 1