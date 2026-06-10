#====File-Handling====
#Syntax
#file = open('filename.txt', 'mode')
'''
external file, internal file, logical file,

internal file - file pointer
external file - .txt
'''
#====MODE====
# # r(read), a(append), w(write)
# file = open("geek.txt", "r")
# # Perform file operations
# file.close()

f = open("geek.txt.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

with open("geek.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")