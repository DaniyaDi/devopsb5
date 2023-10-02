
# John wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# John needs to walk 10000 steps daily  OR needs to run at least
# 4 miles a day.  and Addition to these , John needs eat less 
# than 1500 calories daily. We should create a program to calculate 
# if John can loose weight or not 
# daily steps, running distance and daily calorie intake will be given by user

#There is 2 factors to loosing weight 1 is a movement, second is calorie intake

run_dist =int(input("Enter runnung distance a day in miles:"))
steps = int(input("Enter daily steps amount:"))


is_active =run_dist >= 4 or steps >= 10000

#calorie intake
daily_intake = int(input("Enter daily calories amount:"))
is_intake = daily_intake < 1500
#What should the logical operator be between the is_intake and is_active?

weight_loss = is_intake and is_active
# weight_loss = (run_dist >= 4 or steps >= 10000) and daily_intake < 1500

print(weight_loss)










