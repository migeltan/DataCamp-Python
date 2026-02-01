#for loop
'''
syntax:
for variable in sequence:
    expression
    
'''
fam = [1.73, 1.68, 1.71, 1.89]

#   arbitrary, this is the index
for height in fam:
    print (height)
    
#could also be:
for index, height in enumerate(fam):
    print('index' + str(index), ": " + str(height))
    #converts index and height as strings to be printed 

for c in 'family':
    print(c.capitalize())   #capitalize per letters
 
 
# accessing in a list   
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]       
# Build a for loop from scratch

for room in house:
    room_name = room [0]
    room_area = room [1]
    print("the " + room_name + ' is ' + str(room_area) + ' sqm')