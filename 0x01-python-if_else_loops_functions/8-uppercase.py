#!/usr/bin/python3
# 8-uppercase.py
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
