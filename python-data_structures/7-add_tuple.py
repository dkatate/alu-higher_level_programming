#!/usr/bin/python3
"""Write a function that adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    # make sure each tuple has atleast 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Take only the first 2 elements from each tuple
    a = a[:2]
    b = b[:2]

    # Add the corresponding elements
    first = a[0] + b[0]
    second = a[1] + b[1]

    # Return the result as new tuple
    return (first, second)
