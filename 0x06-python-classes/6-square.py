def __init__(self, size=0, position=(0, 0)):
    """
    Initializes a new square.

    Args:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """
    self.__size = size
    self.__position = position

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

@property
def position(self):
    """
    Gets or sets the position of the square.
    """
    return self.__position

@position.setter
def position(self, value):
    if (
        not isinstance(value, tuple)
        or len(value) != 2
        or not all(isinstance(num, int) for num in value)
        or not all(num >= 0 for num in value)
    ):
        raise TypeError("Position must be a tuple of two non-negative integers.")
    self.__position = value

def area(self):
    """
    Calculates and returns the area of the square.
    """
    return self.__size ** 2

def my_print(self):
    """
    Prints the square using '#' characters.
    """
    if self.__size == 0:
        print("")
        return

    for _ in range(self.__position[1]):
        print("")

    for _ in range(self.__size):
        print(" " * self.__position[0] + "#" * self.__size)
