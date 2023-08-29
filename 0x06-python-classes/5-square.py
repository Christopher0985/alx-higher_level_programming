#!/usr/bin/python3
"""Definition of the Square class."""


class Square:
    """Representation of a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be non-negative")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character."""
        for _ in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
