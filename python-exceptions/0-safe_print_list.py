#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """print number"""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception:
            break
        else:
            count += 1
    print()
    return count
