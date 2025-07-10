#Example 1: Sentence Cleaner

import re

def clean_text (text):
    #removes punctuations
    text = re.sub (r"[^\w\s]", "", text)
    
    #removes extra spaces
    text = " ".join(text.split())
    
    #convert to lowercase
    return text.lower()

input_text = "   Hellow world  .!!! Welcome to python programming,,,   "

cleaned_text = clean_text(input_text)

print("Cleaned Text: ", cleaned_text)
    
    
#Example 2: Palindrome

def is_palindrome(text):
    #removes alphanum and converts to lower
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text [::-1]

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print (f'"{input_text}" is a palindtrome.')
else:
    print (f'"{input_text}" is not a palindrome.')