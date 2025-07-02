#!/usr/bin/python3


def safe_print_division(a, b):
    """divides 2 integers"""
    try:
        result = a/b
    except Exception:
        result = None
    finally:
        print("Inside result: ", result)
    return result
