#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """This function prints an integer with "{:d}".format().

If a ValueError is raised, an appropriate error message is
printed to the standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
