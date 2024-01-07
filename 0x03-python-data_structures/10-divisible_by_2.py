#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []

    else:
        div_2_list = [items % 2 == 0 for items in my_list]

    return div_2_list
