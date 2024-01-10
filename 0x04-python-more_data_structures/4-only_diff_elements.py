#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    no_matches = set_1 ^ set_2
    return no_matches
