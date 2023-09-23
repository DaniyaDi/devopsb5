
# Suppose you have a box containing 28 colored 
# pencils,  and you want to divide them evenly 
# among 5 friends so that each friend gets 
# the same number of pencils.

num_pensils, num_friends = 28, 5

print(num_pensils//num_friends, " friends will have the same amount of pensils")
print(num_pensils%num_friends, " pensils left to me")


#YUSUF's Version
# Suppose you have a box containing 28 colored 
# pencils,  and you want to divide them evenly 
# among 5 friends so that each friend gets 
# the same number of pencils.
# Find out how many pencil each friend will get and 
# also find out how many pencil will be left to you.

num_pencils, num_friends = 28, 5

pencil_per_friend = num_pencils // num_friends

print("Each friend will get",pencil_per_friend,"pencils.")

left_over_pencils = num_pencils % num_friends

print("I will be left with",left_over_pencils,"pencils.")


















