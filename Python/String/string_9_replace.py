
# Given a string, print a version where all 
# the “x” have been removed.
# Except an “x” at the very start or
# end should not be removed.
# example outputs for a given string values
# “xxHxix” → “xHix”
# “abxxxcd” → “abcd”
# “xabxxxcdx” → “xabcdx”

# will the first and last letter in string ever change?
# Isolate the first and last letter

str = input("enter a string:")
first_letter = str[0]
last_letter = str[-1]

# Get the string without the first and last letter
mid_str =str[1:-1].replace('x', '')

new_version = first_letter + mid_str + last_letter
print(new_version)






