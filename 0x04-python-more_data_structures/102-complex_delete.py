#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Delete all keys with a specific value from the dictionary."""
    keys_to_delete = list(a_dictionary.keys())

    for key in keys_to_delete:
        if value == a_dictionary.get(key):
            del a_dictionary[key]

    return a_dictionary
