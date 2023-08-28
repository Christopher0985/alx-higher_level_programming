#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Safely prints the first x integer elements from a list.

    Args:
        my_list (list): The list from which to print integer elements.
        x (int): The maximum number of elements to print.

    Returns:
        int: The count of successfully printed integer elements.
    """
    count_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count_printed += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count_printed
