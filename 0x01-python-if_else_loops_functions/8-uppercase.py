#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase."""
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
