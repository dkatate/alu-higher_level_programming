#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers in a list."""
    count = 0
    try:
        for i in range(x):
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                count += 1
    except Exception:
        pass
    print()
    return count
