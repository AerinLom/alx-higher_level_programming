#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    multiplied_dictionary = dict(a_dictionary)

    for key, values in multiplied_dictionary.items():
        multiplied_dictionary[key] = values * 2

    return multiplied_dictionary
