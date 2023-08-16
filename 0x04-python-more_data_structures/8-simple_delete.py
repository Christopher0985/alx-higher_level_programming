#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Delete a key and its corresponding value from the dictionary if present."""
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
