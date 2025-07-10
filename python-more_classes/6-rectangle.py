#!/usr/bin/python3
"""Define a Rectangle class with width, height, and useful methods."""


class Rectangle:
    """Represents a rectangle with width and height."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and update instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return a string of '#' drawing the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return code-like string to recreate this Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Behave when Rectangle is deleted, decrement count and print."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate and set width; must be int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate and set height; must be int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle's perimeter (or 0 if width/height is zero)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
