#       0123456789..
text = "Python is a programming language"

substr = text[2:6]
print(substr) # thon
print(type(substr)) # class 'str'

# Give me the slicing index numbers to get word programming 
prg = text[12:23]
print(prg) #programming

str2 = "simple"
print(str2[2:100]) # when ending index is bigger than the 
#last index, slicing will not generate an error.
# it will simple get the part of the string from starting index
# to end of the string.

print(str2[2000:4000]) # Empty string -> ''OR''
print(str2[4:2])       # Slicing function will ALWAYS work 
# left to right UNLESS there is negative steps involved.

# Which numerical value will evaluate to True when
# converted to boolean?  - anything except 0

# What happens when we convert strings to bool?
# any string except an empty string will evaluate to True, except an empty string.

str3 ="DevOps"
b = bool(str3[2:10])
print(b) # True
b = bool(str3[22:1])
print(b) # False, because str3[22:1] evaluates to an empty string

################################################################################
# Omitting (Leaving empty) Start or end index when using slicing.
# If you omit start index it will start at index 0, and 
# if you omit ending index, it will go till end of string.

#    012345
s = "python"
print(s[1:]) # ython

print(s[:4]) # pyth

print(s[:])  # python

print("tech"[:]) # tech













