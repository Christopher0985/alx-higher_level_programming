#!/usr/bin/python3
"""Definition of the MagicClass as specified in Holberton's bytecode."""


import math


class MagicClass:
    """Representation of a circle using the MagicClass."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("Radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
