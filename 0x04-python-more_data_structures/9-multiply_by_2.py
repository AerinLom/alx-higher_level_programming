#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    multiplied_dictionary = dict(a_dictionary)

    for key, values in multiplied_dictionary:
        multiplied_dictionary[key] = 2 * values

    return multiplied_dictionary
