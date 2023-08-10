#!/usr/bin/python3
import string
output = getattr(string, 'ascii_uppercase')
exec(__import__('builtins').__dict__['print'](output))
