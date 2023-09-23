#In the farm we have 35 cows , 23 chickens,
#and 40 ducks.
#Create a program to calculate total number of
#legs in the farm
#Requirements create a variable for 
#cows, chickens and ducks , and create variables
#for their number of legs. 
#print "We have 'result' legs in the farm"


cows = 35
chickens = 23
ducks = 40

cows_leg = 4
chickens_leg = 2
ducks_leg = 2

total_cows_legs = cows * cows_leg
total_chickens_legs = chickens * chickens_leg
total_ducks_legs = ducks * ducks_leg

total_num_of_legs = total_cows_legs + total_chickens_legs + total_ducks_legs

print("We have", total_num_of_legs, "legs in this farm") 
# NOTE: Python is going to add space when is
# used in print function.

