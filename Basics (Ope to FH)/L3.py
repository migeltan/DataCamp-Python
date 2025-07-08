#List, Tuples, and Dictionary

#Line 3 to 28 are for LISTS
#This is similar to arrays in C
#List of comma-separated values enclosed in square brackets
#Lists can contain different data types
#Lists are mutable, meaning you can change their content

list1 = ['Physics', 'Chemistry', 1997, 2000];
list2=[1,2,3,4,5]
list3= ["a", "b", "c", "d", "e"]

list1[2] = 2001  # update an element, from 1997 to 2001
print("list1[2]: ", list1[2]) #Accesses 3rd element

BasicListOperations ="""
Basic List Operations:
1. len([1,2,3]) - Number of lists (strlen)
2. [1, 2, 3] + [4, 5, 6] - Concatenation of lists (strcat)
3. ['Hi!' * 4] - Repeats list 4 times (str_repeat)
4. 3 in [1,2,3] - Membership test (strchr)
5. for x in [1,2,3]: print(x) - Iteration over list (strtok)
"""
print(BasicListOperations) #prints nasa taas (triple quotes)

#Accessing list, uses square brackets for slicing along with
#the index of the element.
#Updating a list, you can add them using append() method

#Tuples
#Similar to lists, but immutable
#Uses parentheses instead of square brackets
#Tuples are immutable, whi