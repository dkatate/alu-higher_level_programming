#!/usr/bin/python3
"""Defines a Rectangle class with width, height, drawing, area, and perimeter."""


class Rectangle:
    """Represent a rectangle with validated width and height."""

    def __init__(self, width=0, height=0):
        """Initialize width and height using property setters."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the rectangle's width."""
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
        """Return the rectangle's height."""
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
        """Return the area (width × height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter (2 × (width + height)), or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def _draw_rectangle(self):
        """Return a string representation of the rectangle using '#' characters."""
        result = ""
        for row in range(self.__height):
            result += "#" * self.__width
            if row < self.__height - 1:
                result += "\n"
        return result

    def __str__(self):
        """Return the rectangle’s drawing when printed."""
        return self._draw_rectangle()

    def __repr__(self):
        """Return a string that could recreate this Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
