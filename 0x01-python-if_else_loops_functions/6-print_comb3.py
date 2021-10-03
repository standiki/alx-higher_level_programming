#!/usr/bin/python3
for num in range(9):
    for i in range(num + 1, 10):
        if num != 8 or i != 9:
            print("{:d}{:d}".format(num, i), end=", ")
        else:
            print("{:d}{:d}".format(num, i))
