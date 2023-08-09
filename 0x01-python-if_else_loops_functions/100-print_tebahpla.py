#!/usr/bin/python3
# 100-print_tebahpla.py

for char in range(122, 96, -1):
    print("{}".format(chr(char)), end="")
    char -= 32
    if char >= 97:
        print("{}".format(chr(char)), end="")
