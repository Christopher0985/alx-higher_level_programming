#!/usr/bin/python3
# 100-print_tebahpla.py

"""Print the alphabet in reverse order, alternating uppercase and lowercase."""
toggle = 0
for char_code in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char_code - toggle)), end="")
    toggle = 32 if toggle == 0 else 0
