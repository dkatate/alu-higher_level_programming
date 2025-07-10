#!/usr/bin/python3
"""
This is the "Rectangle" module.
It provides a Rectangle class.
"""


class Rectangle:
    """A Rectangle class with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle's area (width × height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter (2×(width+height)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def _draw_rectangle(self):
        """Return a string of '#' characters representing the rectangle."""
        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __str__(self):
        """Provide a printable representation of the rectangle."""
        return self._draw_rectangle()

    def __repr__(self):
        """Return code-like string to recreate this Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a Rectangle is deleted."""
        print("Bye rectangle...")
