#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a new list with element"""
    # Step 1: Make a copy of the original list
    new_list = my_list.copy()

    # Step 2: Check if idx is valid
    if idx < 0 or idx >= len(my_list):
        return new_list

    # Step 3: Replace the element in the new list
    new_list[idx] = element
    return new_list
