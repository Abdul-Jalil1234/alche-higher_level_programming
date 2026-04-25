#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# The last digit is usually number % 10, but in Python,
# % on a negative number returns a positive result that 
# maintains the cyclic pattern (e.g., -1 % 10 = 9).
# To get the absolute last digit as specified in most C-style 
# logic tasks, we use the absolute value then restore the sign.
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
