
# Formatting is a sort of a short cut to add values from other 
# data types in to string.

# There is 2 ways we could format string.
# *1 using format method.
# Ex: we will put curly braces in a string,
# and those curly braces will be replaced by an argument
# that we put in format method.

s = "Today wheather is {} farenheit."
print(s) #

print(s.format(84)) # Today weather is 84 farenheit.
print(s.format("eighty four")) # Today wheather is eighty four farenheit.

# Note! We could use more than one curly brace to format
# strings, as well as using index for curly braces.

age = int(input("enter your age:"))
name = input("enter your name:")
s2 = "My name is {} and my age is {}."
print(s2.format(name,age))

s3 =" The brand of the laptop is {1}, and model year is {0}"

print(s3.format(2019, "Linux"))

# Second way to format string is using f-strings.
# We still use curly braces but this time we add 
# the name of variables inside the curly braces.

fahr = 84
s =f"Today weather is {fahr} farenheit."
print(s) # Today weather is 84 farenheit.



