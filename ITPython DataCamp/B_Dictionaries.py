#dictionaries part 1
#Keeps track
""""
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", 'albania', "algeria"]
ind_alb = countries.index ("albania")
pop[ind_alb]
"""
#to this: curly braces for dict
#separate through colons
world = {'afghanistan':30.55, "albania":2.77, "algeria":39.21}
world["albania"] #key
#shows string and equiv

#example:
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# Get index of 'germany': ind_ger
ind_ger = countries.index('germany') #index na sha
new = capitals[ind_ger]
# Use ind_ger to print out capital of Germany
print(new)

#printing keys a pain
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# Print out the keys in europe
print(europe.keys())
# Print out value that belongs to key 'norway': prints oslo
print(europe['norway'])


#part 2: dict
# key should be unique
# keys are immutable, but dicts are
# indexed by unique keys unlike lists which are indexed by range of numbers
# used for lookup tables
world["sealand"] = 0.000027 #adds it to the list
print(world)
#change value:
world['sealand'] = 0.000028
print(world)
#remove in lists:
del(world['sealand'])
print(world)

#example:
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# Add italy to europe
europe['italy'] = 'rome'
# Print out italy in europe
print('italy' in europe) #prints if true
# Add poland to europe
europe['poland'] = 'warsaw'
# Print europe
print(europe)

#adding through sub-dictionary:
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
print(europe['france'])

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}
# Add data to europe under key 'italy'
europe['italy'] = data
print(europe)