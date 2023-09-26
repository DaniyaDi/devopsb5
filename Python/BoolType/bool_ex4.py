
#We should create a program to calculate if there is still a ticket 
# for the game tonight. We are given two variables: Capacity of the stadium 
#and the amount of tickets sold. 
# Print True if I can still buy a ticket, False otherwise.
# Note! User will enter the capacity and amount of tickets sold.

stadium_capacity = int(input("Please enter the stadium capacity:"))
sold_tickets = int(input("Please enter the amount of tickets sold:"))

if_space = stadium_capacity > sold_tickets

print("There's space for the game tonight:", if_space)





