#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position"""
    # Check if the index is valid
    if idx < 0 or idx >= len(my_list):
        return my_list

    # If valid, replace the element
    my_list[idx] = element
    return my_list
