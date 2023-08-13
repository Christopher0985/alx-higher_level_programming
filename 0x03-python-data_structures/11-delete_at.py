#!/usr/bin/python3
# File: 11-delete_at.py

def delete_at(lst=[], position=0):
    """Remove an element at a specified position in a list."""
    if 0 <= position < len(lst):
        del lst[position]
    return lst
