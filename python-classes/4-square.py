#!/usr/bin/python3
"""
Module defining a Square class.
"""


class Square:
    """Define a square with a private size."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get current size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
