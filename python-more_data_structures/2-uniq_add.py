#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds"""
    sum_num = 0
    for num in set(my_list):
        sum_num += num
    return sum_num
