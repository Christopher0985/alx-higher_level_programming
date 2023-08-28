#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Safely prints an integer using the "{:d}".format() method.

    If a ValueError is caught, an appropriate message is printed to standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        Returns True if the printing is successful; otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        error_message = "Exception: {}".format(sys.exc_info()[1])
        print(error_message, file=sys.stderr)
        return False

