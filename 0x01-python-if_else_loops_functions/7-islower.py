#!/bin/usr/python3
"""Function that checks for lowercase character"""
def islower(c):
    for letter in range(97, 123):
        if letter == ord(c):
            return True
        else:
            return False
