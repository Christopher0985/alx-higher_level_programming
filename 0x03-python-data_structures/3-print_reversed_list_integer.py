#!/usr/bin/python3
# File: 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Print the integers in a list in reversed order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
