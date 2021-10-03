#!/usr/bin/python3
# function that prints a string in uppercase

def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(c) < 122:
            c = chr(ord(c) - 32)

        print("{:s}".format(c), end="")

    print("")
