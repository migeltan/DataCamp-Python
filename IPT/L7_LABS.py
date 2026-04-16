#====MODULES====

#====List and Tuples====
#Modifying an element
a = [1, 2, 4, 4, 3, 3, 3, 6, 5]
a[3] = 77
print(a)

#Tuples - immutable, uses parentheses
b = (0, 1, 2, 3)
b[0] = 4
print(b)

#Memory efficiency test
import sys #module
a = []
b = ()

a = ["Geeks", "For", "Geeks"]
b = ("Geeks", "For", "Geeks")
        #function
print(sys.getsizeof(a)) #consumes more memory because its mutable
print(sys.getsizeof(b))

#====COMPARISON OF LIST AND TUPLE IN TIME COMPLEXITY====
import time
# Creating a large list and tuple
a = list(range(100000001)) 
b = tuple(range(100000001)) #contiguous memory block

# Timing list iteration
start = time.time_ns()
for i in range(len(a)):
    x = a[i]
end = time.time_ns()
print(end - start) #acts as linked list, mutable

# Timing tuple iteration 
start = time.time_ns()
for i in range(len(b)):
    x = b[i]
end = time.time_ns()
print(end - start) #acts as array since its immutable


#====INDEXING====
a = [1, 2, 3] # list 
b = (4, 5, 6) # tuple

print(a[0]) 
print(b[1])

#====SLICING====
a = [1, 2, 3, 4, 5]
b = (6, 7, 8, 9, 10)
        #START : END
print(a[2:3])
print(b[:1])
'''
SLICING
DOMINGO, TAN, BAUTISTA, EUGENIO, ANOSA, NUESCA, TAMBO, ARJONA
ISIDRO, BAQUING, CARANYAGAN, SANDOVAL, NACUBUAM, SABIO, IGNACIO
MAURING, BASCO, ARAN, PANGANIBAN, MICIANO, MAGTIRA, DIZON, ESCANLLAS
DE ORO, CLERIGO, LIM JC, CORTAS, GILERA, CONCEPCION, DIAMANTE, GONZAGA
PARTIBLE, HERNANDEZ, LURENANA, AVELINO, RAYO, VILLEGAS, WELAN, FLOR, 
VALDEZ, PANES, LIM JIMMY,
'''
#====STRING SLICING====
b = "Hello, World!"
print(b[6:7])

'''
STRING SLICING
EUGENIO, WELAN, ISIDRO, HERNANDEZ, MAURING, DOMINGO, LIM, NUESCA,SANDOVAL
BASCO, DIZON, ANOSA, GILERA, ARAN, CONCEPCION, IGNACIO, BAQUING, PANGANIBAN,
MAGTIRA, TAN, MICIANO, BAUTISTA, CARANYAGA, SABIO, SILVERIO, ARJONA, DE ORO,
CORTAS, VALDEZ, NACUBUAN, AVELINO, CLERIGO, PANGANIBAN 
'''

#====CONCATENATION====
# List Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# Tuple Concatenation
a = (7, 8, 9)
b = (10, 11, 12)
print(a + b)

#====LIST SPECIFIC OPERATIONS====
a = [1, 2, 3]

a.append(4) #adds element at the end
a.extend([5, 6])  #merges listt
a.remove(2) #removes ng first occurence ng 2
a.append(7)
a.extend([8,9])
a.remove(1)
print(a)