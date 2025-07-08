#String Manipulation

#Concatenation - combining different strings (+)

first = "Hello"
second = " World!"

result = first + second
print (result)

#Slicing - extracting part of a string (:)

text = "Python Programming"
first1= print (text[0:6])
second2 = print (text[-11:])
# result2 = first1 + second2
# print (result2)

#Formatting 
name = "Migel"
age = 19
print(f"My name is {name} and I am {age} years old.") #f for formatting

#String methods
"""
    split (), join (), replace(), strip()
"""

#split()
sentence = "Python is fun"
words = sentence.split()
print (words)

#join() - joins to a single string

new_sentence = " ".join(words)
print(new_sentence)

#replace ()
text = "I love C"
updated_text = text.replace("C", "Python")
print(updated_text)

#strip()
messy = "       hellow, world!   "
cleaned_text = messy.strip() #strips space
print(cleaned_text)

#Regular expressions for pattern matching 
"""
Regular Expressions - way to search and manipulate based on pattern
- domain, etc. pattern you follow.
- using re Module

Common Functions:
    1. re.search (pattern, string) - searches for a pattern for a string
    2. re.findall (pattern, string) - List all occurences
    2. re.sub(pattern, replacement, string) 
"""

import re # r for formatting

#findall
text = "Contact me at 0923-106-2306"
digits = re.findall (r"\d+", text)
print(digits)

#sub
updated_text = re.sub (r"\d", "X", text) #replaces whatever
print(updated_text)


