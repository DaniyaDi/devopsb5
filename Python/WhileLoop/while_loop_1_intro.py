
# Lets create a loop to print numbers from 1 to 5 
# We have to be doing something that would eventually change the condition.
num = 1 
while num <= 5:
    print(num)
    num += 1
print(f"Value of the variable num after the loop is {num}")


#Let's create a program that will print all numbers from 20 to 1 inclusive

num = 20
while num > 0:
    print(num)
    num -= 1

# Lets create a program that will print numbers from 1 to 10
# for even numbers it will say 'num is even'
# for odd numbers it will say 'num is odd'

num = 1 
while num <= 10:
    if num % 2 == 0:
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number.")
    num += 1 











