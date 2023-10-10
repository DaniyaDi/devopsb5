
# Task1
# Given a string, if the first or last chars are 'z', 
# print the string without those 'z' chars, and
# otherwise print the string unchanged.

# "zHiz" → "Hi"
# "zHi" → "Hi"
# "Hziz" → "Hzi"
# "zzHizz" → zHiz

str = input("Please enter a string:")
if str.startswith("z"):
    str = str[1:]
if str.endswith("z"):
    str = str[:-1]
    print(str)

# Better solution

str = str.removeprefix("z")
str = str.removesuffix("z")
print(str)

