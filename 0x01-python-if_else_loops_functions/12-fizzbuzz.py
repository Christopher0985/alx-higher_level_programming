#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """Print numbers from 1 to 100, replacing certain multiples.

    For numbers divisible by three, print Fizz; by five, print Buzz;
    and by both three and five, print FizzBuzz.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
