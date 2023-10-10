
# Find method will return us the lowest index of a given character
# or sequence of characters.

s = "Techtorial Academy"

print(s.find("a")) # 8
print(type(s.find("a"))) # <class 'int'>


print(s.find("b")) # -1
print(type(s.find("b"))) # <class 'int'>
print(s.find("de")) # 14
print(s.find("ac")) # -1  there is no sequence "ac" in a string"
print(s.find("Techtorial")) # 0

# Get only "Techtorial" from the string
print(s[:10])  # type of slicing is string. 











