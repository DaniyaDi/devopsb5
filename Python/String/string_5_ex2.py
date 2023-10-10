
# ask user to enter their age, if they enter anything
# bigger than 2 digit numbers and if they don't enter
# a number print "invalid age"
# print "okay"

age = input("enter your age, please:")
# What id the data type of age?
# it is a string!
# How we can understand, use len 

b1 = 0 < len(age) <= 2 # we make sure user entered 
# more than 0 and less than equals 2 characters.

# How can I check if the string consist of numbers only?
# age == age.upper()
# age == age.lower()

b2 = age == age.upper() and age == age.lower() 

if b1 and b2:
    print("Your age is:", age )
else:
    print("Your age is not valid")



