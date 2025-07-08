#Exercise 1: Manipulate Data in a Dictionary

person = {"name": "Migel", "age": 19, "grade": 1.15}
#add new key value
person ["address"] = "23 Lahuerta"

#update age
person ["age"] = 20

#remove grade
if "grade" in person:
    del person ["grade"]
    
print(person)

#Exercise 2: Word Frequency Counter

sentence = input ("Enter a Sentence: ")

#Split the sentence into words

word = sentence.split()

#initialize a dictionary
word_count = {}

#count word frequency
for words in word:
    words = words.lower() #for case sensitivity
    if words in word_count:
        word_count[words] +=1
    else:
        word_count [words] = 1
        
print (word_count)