
# There are 20 devops in the company that should be 
# equally assigned to each 8 scrum teams.
# Find out how many of them wont be assigned with a team
# Also find out how many devops engineers will be in 
# each of scrum team 

# In order to find number of devops engineers in each team 

num_devops, num_teams = 20, 8
print("Each team will have", num_devops//num_teams, "devops engineers.")

print ("After the assignment there will be", num_devops%num_teams, "engineers unassigned.")





