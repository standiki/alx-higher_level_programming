#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastDigit = int(number % 10) if number >= 0 else int(-(-number % 10))

if lastDigit > 5:
    print("Last digit of {} is {} and is greater 5".format(number, lastDigit))
elif lastDigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastDigit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastDigit))
