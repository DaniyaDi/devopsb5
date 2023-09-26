
# Company wants to increase their server according to their CPU usage. 
# Create a python program that gets average cpu usage as an input 
# and prints True if we need to launch more servers for our application.
# When average cpu usage is between 40 and 70 inclusive
# we should launch a new server.

cpu_usage = int(input("Please enter average cpu usage:"))
if_usage = 40 <= cpu_usage or 70 <= cpu_usage
print("Company should launch a new server", if_usage) 





