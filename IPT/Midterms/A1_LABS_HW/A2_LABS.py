#Assignment #2: Write a program to print all ASCII character with their values.
#A-Z, a-z, 0-9

print("Uppercase Letters (A-Z): ")
for char in range(ord('A'), ord('Z') + 1):
    print(chr(char), "=", char)

print("\nLowercase Letters (a-z): ")
for char in range(ord('a'), ord('z') + 1):
    print(chr(char), "=", char)

print("\nDigits (0-9): ")
for char in range(ord('0'), ord('9') + 1):
    print(chr(char), "=", char)

print("\nSpecial Characters: ")
for char in range(58, 65):
    print(f"{chr(char)} = {char}")