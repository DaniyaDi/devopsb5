
# input function allows us to work with dynamic values.
# because values will be given by user when the code runs.
# Input function will always give the data as text(string), so we should
# convert it according to what we need using function like (int(), float(), bool())

# Example of using input function 

var1 = int(input("Enter your age:") )


print("The user's age is", var1) # This will print users input.
print(type(var1)) # Type will be <class 'str'> (text)

# Print true if the user is older than 21, print false otherwise.

is_older = var1 > 21
print("is user bigger than 21?", is_older)




