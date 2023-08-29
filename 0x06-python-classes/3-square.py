#!/usr/bin/python3
"""Definition of the Square class."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be non-negative")
        self.__size = size

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size * self.__size
