#Example 2:
#Please enter your balance:
#5.22
#Output:
#$5.22 will make 20 quarters 2 dimes 0 nickels and 2
#pennies

balance = 5.22
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

print("5.22 will make",qrtrs_amount, "quarters", dms_amount, "dimes", nickels_amount, "nickels", pnns_amount, "pennies")
