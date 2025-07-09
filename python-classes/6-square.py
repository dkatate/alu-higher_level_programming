#!/usr/bin/python3
"""Defines a Square with size and position, with area and custom printing."""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size            # invokes size.setter
        self.position = position    # invokes position.setter

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' respecting size and position."""
        if self.__size == 0:
            print()
            return

        # Vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            # Horizontal spaces (position[0]) then size times '#'
            print(" " * self.__position[0] + "#" * self.__size)
