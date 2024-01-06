#!/usr/bin/python3

def no_c(my_string):

    updated_string = ""

    for letters in my_string:
        if letters != 'c' and letters != 'C':
            updated_string += letters

    return updated_string
