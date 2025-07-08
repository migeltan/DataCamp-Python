#Lists - ordered mutable collections that can hold varieties
#of data types.

numbers = [1,2,3,4]
fruits = ["apple", "banana", "cherry"]
mixed = [1, 2, 3, "true", False]

#slicing
sliced_fruits = fruits [1:3]
print(sliced_fruits)

# print(numbers[2])
# print(fruits[0:2]) #accessing through index

# print(fruits[-1]) #negative indexing

# #adds
# fruits.append ("orange")
# fruits.insert (1, "grape") #inserts between apple and banana
# print (fruits)

# #remove
# fruits.remove("banana")
# print (fruits)

# del fruits [0] #deletes through index
# print(fruits)

# fruits.pop #deletes last item
# print(fruits)

#Tuples - ordered immutable collection of items
colors=("Pink", "Green", "Blue")
single_tuple = ("glass",) #for single tuple, add comma still

#access
print (colors[0]) #first color


# Dictionaries - store key values for fast look up
student = {"name": "migel", "age": 19, "grade": 1.15}
print (student)
print (student["name"]) #access the pair

#adding
student ["subject"] = "math"
student ["age"] = 32
print(student)

#removing 
del student ["grade"]
print(student)

student.pop("subject")
print(student)

#iterate
for key, value in student.items():
    print(key, value)
    
    
#Sets - unordered collection of unique items
numbers = {1, 2, 3, 4}
empty_set = set()

#add and remove
numbers.add(5) #doesnt add duplicates
print(numbers)

numbers.remove(2)
print(numbers)

#Set Operations : Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print (set1 | set2) #pipe operator for union

#Set Operations : Intersection
print (set1 & set2)

#Set Operations : Difference
print (set1-set2)

