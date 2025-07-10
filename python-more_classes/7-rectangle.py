#!/usr/bin/python3
"""Define a Rectangle class with width."""


class Rectangle:
    """Represents a rectangle defined by width and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle and update instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return the rectangle drawn with `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = [
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string that recreates the rectangle if evaluated."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """On deletion, decrease count and print a goodbye message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieve the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width ensuring it's an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height ensuring it's an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle's perimeter, or 0 if either """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
