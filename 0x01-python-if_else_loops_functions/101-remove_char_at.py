#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(s, n):
    new_str = ""
    for i in range(len(s)):
        if i != n:
            new_str += s[i]
    return new_str
