#Write a Java program to convert minutes into a number of years and days.
#Test Data
#Input the number of minutes: 3456789
#Expected Output :
#3456789 minutes is approximately 6 years and 210 days

num_minutes = 3456789

one_hour = 60
one_day = 60 * 24
one_year = one_day * 365

year_count = num_minutes // one_year
remaining = num_minutes - year_count * one_year
day_count = remaining // one_day

print("3456789 minutes is approxiamately", year_count, "years and", day_count, "days")