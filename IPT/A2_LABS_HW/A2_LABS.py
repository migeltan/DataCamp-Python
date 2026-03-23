'''A default argument is a parameter that assumes a 
default value if a value is not provided in the function call for 
that argument.'''

#   func name   formal parameter 
def my_function(name = "friend"): #friend is the default value defined sa func heading
  print("Hello", name)            #parameter pass

my_function("Emil") #actual parameter
my_function("Tobias")

my_function() #itll print friend since walang na-assign na argument sa function call

my_function("Linus")

#Default Argument