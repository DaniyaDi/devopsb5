#Create a program that will add up the value of a number 
#of quarters, dimes, nickels, and pennies. 
#The number of each type of coin is input by the user. The total value is printed in dollars.
#Example: Quarters: 5 Dimes: 4 Nickels: 3 Pennies: 2
#he total in dollars is $1.82


quarterts, dimes, nickels, pennies = 0.25, 0.1, 0.05, 0.01

num_1 = int(input("Enter number of quarters:"))
num_2 = int(input("Enter number of dimes:"))
num_3 = int(input("Enter number of nickels:"))
num_4 = int(input("Enter number of pennies:"))

print("The total amount in dollars is $", quarterts * num_1 + dimes * num_2 + nickels * num_3 + pennies * num_4)
# The total amount in dollars is $ 1.8199999999999998 
# so below i decided to * to 100


qrtrs_mult, dimes_mult, nickels_mult, pennies_mult = 0.25*100, 0.1*100, 0.05*100, 0.01*100
num1_1 = int(input("Enter number of quarters:"))
num_2_2 = int(input("Enter number of dimes:"))
num_3_3 = int(input("Enter number of nickels:"))
num_4_4 = int(input("Enter number of pennies:"))
total_cents_mult = qrtrs_mult * num1_1 + dimes_mult * num_2_2 + nickels_mult * num_3_3 + pennies_mult * num_4_4

print("The total amount in dollars is $", total_cents_mult / 100)



