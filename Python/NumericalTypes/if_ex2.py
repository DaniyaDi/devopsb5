
# create a program that asks a user an integer value.
# if this integer value is even double the number and print out the result.
# if the number is odd print (you entered an odd number.)

number =int(input("enter integer value:"))

# We should check if the given number is odd number.
if number % 2 == 0:
    print(number * 2)
elif number % 2 != 0:
    print("you entered an odd number")






