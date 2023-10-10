
# Given a string from user, print the mirror ends.
# abcjkhurbca -> abc
# hannah -> hannah 
# civic -> civic 
# atechtoriala -> a


str = input("enter a string:")

left_to_right_index =  0  # left to right index
right_to_left_index = -1  # right to left index

# left to right index should keep getting bigger
# right to left index should keep getting smaller
mirror_end = ""
while left_to_right_index < len(str):
    # How can I check if the letters for these indexes are matching?
    if str[left_to_right_index] == str[right_to_left_index]:
        mirror_end += str[left_to_right_index] # you could also assign r_to_l
    else:
        break

    left_to_right_index += 1
    right_to_left_index -= 1

print(mirror_end)


