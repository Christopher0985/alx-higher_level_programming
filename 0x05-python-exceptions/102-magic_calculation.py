#!/usr/bin/python3

def magic_calculation(a, b):
    """Performs a calculated operation with error handling.

    Args:
        a (int): First operand.
        b (int): Second operand.

    Returns:
        The calculated result or the sum of a and b if an exception occurs.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a
            break
    return result
