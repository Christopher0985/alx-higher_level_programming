#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to be executed.
        args: Arguments to be passed to fct.

    Returns:
        The result of the function call if successful, otherwise None.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return (None)
