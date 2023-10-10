
# isalnum() (alphanumeric)
# This method will return True if string consists of letters or numbers or combination of both .

s = "text"
s1 = "text1"
s2 = "12345"
s3 = "1!Te"
print(s.isalnum())  # True
print(s1.isalnum()) # True
print(s2.isalnum()) # True
print(s3.isalnum()) # False

#isalpha()
# Will return True if the string consist of only letters.
print(s.isalpha())  # True
print(s1.isalpha()) # False
print(s2.isalpha()) # False
print(s3.isalpha()) # False


s = "text"
s1 = "text1"
s2 = "12345"
s3 = "1!Te"

# isnumeric()
# Will return True if the string consist of only numbers.
print(s.isnumeric()) # False
print(s1.isnumeric()) # False
print(s2.isnumeric()) # True
print(s3.isnumeric()) # False
print(type(s2))       # <class 'str'>

# Return type of these methods is boolean.

# Ask user their age
# if they en

age = input("please enter your age:")
if age.isnumeric() :
    print(f"your age is {age}.")
else:
    print(f"{age} invalid entry")






















