#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list

    elif idx >= len(my_list):
        return my_list

    updated_list = list(my_list)
    updated_list[idx] = element
    return updated_list