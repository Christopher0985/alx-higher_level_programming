#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        # Attempt to use an undefined variable, which will raise a NameError
        undefined_variable
    except NameError:
        raise NameError(message)
