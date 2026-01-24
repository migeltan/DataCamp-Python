#methods- functions that belong to objects.
"""
str has:
capitlaize()
replace()

float has:
bit_length()
conjugate()

list has:
index()
count()  
"""

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
fam.index('mom') #call method index for mom returns 4
fam.count(1.73) #shows how much it has

sister = 'liz'
cap = sister.capitalize()
print(cap)
rep = sister.replace('z','sa')
print(rep)

ind = sister.index('z')
print(ind)

#append
fam.append('bakla')
fam.append(1.68)

print(fam)