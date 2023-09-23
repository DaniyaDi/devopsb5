
# A DevOps team needs to perform 
# a system update on 212 servers. However, 
# they can only update 8 servers per day due to 
# resource restrictions.
# They want to find out how many full 
# days it will take to complete the updates
# and if there will be servers left over on
# the end of final full day.

num_servers_to_update, num_servers_per_day = 212 , 8

print("It will take", num_servers_to_update//num_servers_per_day, "full days to update servers")
print("It will be", num_servers_to_update%num_servers_per_day, "servers left not updated")


#YUSUF's version
# outdated = not updated 


# A DevOps team needs to perform 
# a system update on 212 servers. However, 
# they can only update 8 servers per day due to 
# resource restrictions.
# They want to find out how many full 
# days it will take to complete the updates
# and if there will be servers left over on
# the end of final full day.

servers,daily_updated_servers = 212, 8

full_day = servers // daily_updated_servers
print("They will be doing updates for",full_day,"full days.")

outdated_servers = servers % daily_updated_servers

print("We will have",outdated_servers,"outdated servers at the end.")








