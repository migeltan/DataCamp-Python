#Example 1: Count Words and Lines in a file

# def count_words_lines (filename):
#     try: 
#         with open(filename, "r") as file:
#             lines = file.readlines()
#             line_count = len(lines)
#             word_count = sum(len(line.split()) for line in lines) 
            
#             print(f"Number of lines: {line_count}")
#             print(f"Number of words: {word_count}")
#     except FileNotFoundError:
#         print(f"File {filename} not found!")
        
# count_words_lines ("sample.txt")

#Example 2: Write and Read a list of items

def write_to_file ( filename, items):
    with open (filename, "w") as file:
        for item in items:
            file.write(item + "\n")
            
def read_to_file(filename):
    try:
        with open (filename, "r") as file:
            items = file.readlines ()
            print ("Items in the file are: ")
            for item in items:
                print (item.strip())
    except FileNotFoundError:
        print(f"File {filename} not found!")
        
items = ["Apple", "Banana", "Cherry", "Mango"]
write_to_file ("fruits.txt", items)
read_to_file ("fruits.txt")