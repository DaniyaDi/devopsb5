#Write a program that will take a given amount of money and return 
#the number of dollars in quarters, dimes, nickels, and pennies that make up that given amount
#Example 1:
#Please enter your balance:
#2.36
#$2.36 will make 9 quarters 1 dime 0 nickels and 1 pennies


balance = 2.36
total_cents = balance * 100
quarters = 0.25 * 100
dimes = 0.1 * 100
nickels = 0.05 * 100
pennies = 0.01 * 100

qrtrs_amount = (total_cents // quarters) 
rem_1 = total_cents - qrtrs_amount * quarters
dms_amount = rem_1 // dimes
rem_2 = total_cents - (qrtrs_amount * quarters + dms_amount * dimes)
nickels_amount = rem_2 // nickels
rem_3 = total_cents-(qrtrs_amount * quarters + dms_amount * dimes + nickels_amount * nickels)
pnns_amount = rem_3 // pennies

print("$2.36 will make",qrtrs_amount, "quarters", dms_amount, "dimes", nickels_amount, "nickels", pnns_amount, "pennies")











