
#Ask user to enter an integer number and print if 
#the given integer is a prime integer. 
#Prime numbers can ONLY be divided by 1 and itself. 
# Every number can be divided by one and itself, 
#the distinct feature of prime numbers is not divided by any other number.
# 11 is prime  1 11
# 13 is prime
# 37 is prime 1 37
# 91 is not prime 1 7 13 91

# How can I distinguish prime numbers from other numbers?
# It shouldm't be divided by any number except 1 and itself.

# I should look into all Possible divisors of a number, and make sure 
# none of those divides number perfectly.

# For a number X what are the possible range of divisors?
# 1 to X
# since every number will be perfectly dividible by 1 and itself 
# I should take those out equation.
# According to information above let's update our range of divisors for
# number X
# 2 to X/2 

number = int(input("enter any integer value:"))
# 9 -> because beside 1 and intesl it could also by divisible by 3.

possible_divisor = 2 
is_prime = True
while possible_divisor <= number/2:
    if number % possible_divisor == 0:
        print("It is not a prime.")
        is_prime = False
        break # because there is no reason to continue executing the loop
        # when I already find out given number is not prime.
    possible_divisor += 1
    
if is_prime:
    print(f"{number} is prime number.")






