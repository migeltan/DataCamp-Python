def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")
#error, positional-only arguments passed as keyword arguments