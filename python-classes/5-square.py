#!/usr/bin/python3
"""
Module defining a Square class.
"""


class Square:
    """Define a square with a private size and print behavior."""

    def __init__(self, size=0):
        """Initialize size with validation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square's area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters, ."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)
