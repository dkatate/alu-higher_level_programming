#!/usr/bin/python3
"""Define a Rectangle class with utilities and comparison."""


class Rectangle:
    """Represents a rectangle defined by width and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize width, height, and update instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return a string of `print_symbol` to visually represent the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = [
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string representation that can recreate this Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Run when the instance is deleted—update count and notify."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the larger area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Raises:
            TypeError: If either argument is not a Rectangle.

        Returns:
            Rectangle: The larger rectangle or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width, checking it is an integer ≥ 0."""
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
        """Set height, checking it is an integer ≥ 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle's area (width × height)."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the rectangle's perimeter.
        Returns 0 if either width or height is zero.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
