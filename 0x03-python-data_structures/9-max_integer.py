#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    maximum_val = my_list[0]

    for number in my_list:
        if number > maximum_val:
            maximum_val = number

    return maximum_val
