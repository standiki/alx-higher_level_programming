#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = int(number % 10)
else:
    lastDigit = int(-(-number % 10))
if lastDigit > 5:
    res = "is greater than 5"
elif lastDigit == 0:
    res = "is 0"
elif lastDigit < 6 and lastDigit != 0:
    res = "is less than 6 and not 0"
print("Last digit of {} is {} and {}".format(number, lastDigit, res))
