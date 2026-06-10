''' In keyword arguments, values are passed by explicitly 
specifying the parameter names, so the order doesn't matter. '''

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

            #actual pass via keywords
my_function(animal = "dog", name = "Buddy")
#keyword arguments