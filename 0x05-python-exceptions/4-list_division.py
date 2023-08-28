#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element-wise and handles exceptions.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list of length list_length containing division results.
    """
    result_list = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result_list.append(division)
    return result_list
