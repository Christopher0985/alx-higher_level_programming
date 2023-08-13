#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return (length, first)
