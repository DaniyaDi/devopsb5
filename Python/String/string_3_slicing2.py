
s = 'programming'

print(s[1:10:3]) # -> rrm

# Negative steps
# Slicing function will always work
# left to right unless there is negative steps involved.

print(s[  1  :  10  :  -3  ]) # empty string
# It works right to left

#        start  end   step
print(s[  7  :  1  :  -3  ])  # mrr

t = "techtorial"
print(t[::1]) # techtorial
print(t[::2]) # tctra

print(t[::-1]) # This will return the reversed version of the 
# string


# Negative indexes in python
#     654321 (all these numbers are negative)
#     012345
pl = "python"

print(pl[-1:-3]) # Empty string
# Is steps here positive or not?
print(pl[-1:]) # n 

print(pl[:-3]) # pyt














