#March 16, 2026

#positional-only / standard argu
#left is positional-only of the slash
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Migel"))
print(greet("Kurt", "Hi"))
#requires a positional only argument
print(greet("Charlie", greeting = "Good morning"))
#positional and default argument

#----Function with return statement----
#def function_name (parameter1, parameter2):
#    function body
#    return return_value

def calculate_area(length, width):
    area = length * width
    return area
area = calculate_area (50, 50) #get the result of the function
print(f"Calculated area: {area}") #use the result of the function

#another example
def get_even(numbers):
    even_nums = [num for num in numbers if not num % 2]
    return even_nums

print(get_even([1, 2, 3, 4, 5, 6]))
