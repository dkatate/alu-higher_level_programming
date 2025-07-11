#!/usr/bin/python3
"""
Module that defines a function to check if an object is exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is exactly an instance of a_class (not a subclass), False otherwise.
    """
    return type(obj) is a_class
