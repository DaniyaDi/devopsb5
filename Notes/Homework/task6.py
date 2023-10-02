
#Create two string variables bigger than the length 3.
#If the second string starts with the first string’s last three characters, 
#print true. If not, print false.

string1 = "Techtorial"
string2 ="Chicago"

if string2.startswith(string1[-3:]):
    print("True")
else:
    print("False")


# This one I did with chatgpt, because I don't remember this topic :( I need to go through 