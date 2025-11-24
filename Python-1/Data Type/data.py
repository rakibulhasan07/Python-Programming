# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType




# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

x = "Hello World" #Text Type:	str
#display x:
print("Text Type:	str-",x)
#display the data type of x:
print(type(x))



x = 20 #Numeric Types:	int
#display x:
print("Numeric Types:	int-",x)
#display the data type of x:
print(type(x))


x = 20.5 #Numeric Types:	float
#display x:
print("Numeric Types:	float-",x)
#display the data type of x:
print(type(x))


x = 1j #Numeric Types:	complex
#display x:
print("Numeric Types:	complex-",x)
#display the data type of x:
print(type(x))


x = ["apple", "banana", "cherry"] #Sequence Types:	list | JavaScript Array
#display x:
print("Sequence Types:	list | JavaScript Array-",x)
#display the data type of x:
print(type(x))


x = ("apple", "banana", "cherry") #Sequence Types:	tuple | JavaScript Object
#display x:
print("Sequence Types:	tuple | JavaScript Object-",x)
#display the data type of x:
print(type(x))


x = range(10) #Sequence Types:	range | JavaScript Looping Structure
#display x:
print("Sequence Types:	range | JavaScript Looping Structure-",x)
#convert to list to display the content of x:
print(list(x))


x = {"name" : "John", "age" : 36} #Mapping Type:	dict | JavaScript Object
#display x:
print("Mapping Type:	dict | JavaScript Object-",x)
#display the data type of x:
print(type(x))


x = frozenset({"apple", "banana", "cherry"}) #Set Types:	frozenset | JavaScript Set
#display x:
print("Set Types:	frozenset | JavaScript Set-",  x)
#display the data type of x:
print(type(x))
