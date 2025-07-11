#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
It includes a method to print the list elements in sorted order.
"""


class MyList(list):
    """A subclass of list with an additional method to print sorted list."""

    def print_sorted(self):
        """
        Print the list elements in ascending sorted order.

        The original list is not modified.
        """
        print(sorted(self))
