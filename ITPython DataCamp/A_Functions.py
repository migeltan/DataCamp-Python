#Functions on Python

fam = [1.73, 1.68, 1.71, 1.89]
#uses pre-defined functions
maxheap = max(fam) #passes through the list and prints max.
print(maxheap)

#round - round off
tens = round(1.68, 2) #second is for its place/ndigits
rup = round(1.68) #ceil basically
help(round) 
print (tens, rup)

#checks length
print(len(fam))

#power of
print(pow(10, 2))

#sorts descending due to reverse
maxsort = sorted(fam)
maxsort.reverse()
print(maxsort)

