#File Handling

"""
#Reading and Writing
#Opening: open() - r / w / a / r+
#Reading Files
#.read() / .readline() / .readlines()
"""
#readfiles
# with open("sample.txt", "r") as file:
#     content = file.readline()
#     print (content)
  
# #write files  
# with open("sample.txt", "w") as file:
#     # content = file.readline()
#     # print (content)
    
#     file.write("Hi world!")
#     file.writelines (["Migel", "Reyna", "Bakla"])
#     # file is automatically closed
    
# with statements - to make sure that the files you open are
#properly closed afterwards.

#Basic Exception handling - prevents the program from crashing
#file not found (if file == null)
#FileNotFoundError, PermissionError, IOError

try: 
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print ("File Not Found!")
