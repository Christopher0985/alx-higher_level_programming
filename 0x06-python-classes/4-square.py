#!/usr/bin/python3
"""
This script defines a Square class for representing squares.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets or sets the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be non-negative.")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2


if __name__ == "__main__":
    try:
        square = Square(7)
        print("Square size:", square.size)
        print("Square area:", square.area())

    except Exception as e:
        print("An error occurred:", str(e))
