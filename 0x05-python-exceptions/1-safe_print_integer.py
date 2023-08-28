#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer using the "{:d}".format() method.

    Args:
        value (int): The integer to be printed.

    Returns:
        Returns True if the printing is successful; otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
