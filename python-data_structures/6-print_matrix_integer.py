#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for row in matrix:
        for number in row:
            print("{:d}".format(number), end=" ")
        print()
