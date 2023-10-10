
s = input("enter anything:")
# what is the lenght for the string?
print(len(s))

# what  would be the last(biggest) index number in string above?
biggest_index = len(s) - 1
if biggest_index >= 4:
    print(s[4])
else:
    print("Sorry, but there is no index 4 in string.")


# which index number we should find in string?
# I need to find the letter at index 4
print(s[4])  # this will bring the 5th character in string.

# Note! if the index number we are trying to access doesn't 
# exist in string, it will generate IndexError.

# Refactor this code so that it wouldn't generate an error when 
# user enters a string that doesn't have index 4.

