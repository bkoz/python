#
# Week 3 - Functions
#
def my_function(): 
	"""Demonstrate docstrings and does nothing really."""

	return None

print("Using __doc__:")
print(my_function.__doc__) 

#print("Using help:")
#help(my_function) 

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
