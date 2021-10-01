#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

i = int(number % 10) if number >= 0 else int(-(-number % 10))

if i > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, i))

elif i is 0:
    print("Last digit of {} is {} and is 0".format(number, i))

elif i < 6 and i != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, i))
