
# Ask user to enter a password but there will be conditions,
# our condition for a valid password is:
# 1. it has to have an upper case
# 2. it has to have a lower case 
# If user provides a valid password print "your password" is valid
# otherwise print "password invalid"

password = (input("Please enter your password:"))
# if password equals to user_pass.lower() what do you think?
# A: it would mean og. consists of all lower cases.
# if password equals to user_pass.upper() what do you think?
# A: it would mean og. consists of all upper cases.
# Do we want any one of situation above yo be true?
# A: We don't want both of situations above to be false at
# the same time.

b1 = password != password.lower()
b2 = password != password.upper()

if b1 and b2:
    print("Your password is valid")
else:
    print("Your password is invalid")








