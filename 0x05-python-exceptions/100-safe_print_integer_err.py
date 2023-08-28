#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    This function prints an integer using the format "{:d}".

If a ValueError is raised, an appropriate error message is
printed to the standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        Returns True if the integer was successfully printed,
        and False if a TypeError or ValueError occurred.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        error_message = "Exception: {}".format(sys.exc_info()[1])
        print(error_message, file=sys.stderr)
        return False
