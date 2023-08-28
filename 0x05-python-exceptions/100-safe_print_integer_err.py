#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Safely prints an integer using the "{:d}".format() method.

    Args:
        value (int): The integer to be printed.

    Returns:
        bool: True if printing is successful; False if an exception occurs.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        error_message = "Exception: {}".format(sys.exc_info()[1])
        print(error_message, file=sys.stderr)
        return (False)
