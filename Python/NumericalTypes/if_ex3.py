
# Create a program that calculates the grade letter of a student.
# Ask user their grade in integer number.
# Print `not a valid grade` if the lower than 0 or bigger than 100.
# Print A+ if the grade is higher than 95
# Print A if the grade is in between 85 and 94 inclusive
# Print B if the grade is in between 75 and 84 inclusive
# Print C if the grade is in between 65 and 74 inclusive
# Print grade doesn't meet expectations when the grade is lower than 65.

number = int(input("Please enter your grade:"))
if number > 100 or number < 0:
    print("not a valid grade")
elif number > 94:
    print("A+")
elif 85 <= number <= 94:  
    print("A")
elif 75 <= number <= 84:
    print("B")
elif 65 <= number <= 74:
    print("C")
elif number < 65:
    print("doesn't meet expectations")












