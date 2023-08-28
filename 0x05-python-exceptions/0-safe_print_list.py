#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print a specified number of elements from a list safely.

    Args:
        my_list (list): The list from which to print elements.
        x (int): The number of elements from my_list to print.

    Returns:
        The count of elements actually printed.
    """
    count_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count_printed += 1
        except IndexError:
            break
    print("")
    return count_printed
