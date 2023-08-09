#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the alphabet in small letters without a trailing newline."""
for letter_code in range(97, 123):
    print("{}".format(chr(letter_code)), end="")
