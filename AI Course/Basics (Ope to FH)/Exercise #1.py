#Hands-on
# This is a simple Python script to print "Hello, World!"
# print("Hello, World!")

# Define variables of diff data types
integer_var = 10 #int
#int_year
int_month= 7
int_day= 5

float_var = 3.14 #float

string_var = "AI"
# + concatenates, * repeats, [] slices, [:] range slices

list_var = [1,2,3] #arrays in c
#lists can be accessed using slice operators ([] and [:])

tuple_var = (4, 5, 6) #similar to lists, number of values 
# enclosed by a parentheses, read-only lists

dict_var = {"name": "Migel", "role": "Student"}
#works like an associative arrays.

bool_var = True

print("Twinkle, twinke little star,\n\tHow I wonder what you are!")
print("\t\tUp above the world so high, \n\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are")


#Print and Manipulate variables
print("Integer: ", integer_var)
print("Float: ", float_var)
print("String: ", string_var + " Bootcamp") #Concatenation

list_var.append(4)
print("List: ", list_var) #Prints the list with the new value added
print ("Tuple: ", tuple_var)
print("Dictionary: ", dict_var["name"]) #specified
print("Boolean: ", bool_var)


