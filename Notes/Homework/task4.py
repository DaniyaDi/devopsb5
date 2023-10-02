
number = 53876

last_digit = number % 10
#print(last_digit)
number2 = number // 10
last_digit2 = number2 % 10
#print(number2)
number3 = number2 // 10
last_digit3 = number3 % 10
#print(number3)
number4 = number3 // 10
last_digit4 = number4 % 10
#print(number4)
number5 = number4 // 10
#print(number5)

print(last_digit,last_digit2,last_digit3,last_digit4,number5)

#or this

number = int(53876)
reversed_number = int(str(number)[::-1])
print("Reversed number:", reversed_number)

number = int(97352)
reversed_number = int(str(number)[::-1])
print("Reversed number:", reversed_number)










