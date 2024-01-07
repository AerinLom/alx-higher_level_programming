#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = tuple_a + (0, 0)
    tup_b = tuple_b + (0, 0)
    tup_a = tup_a[:2]
    tup_b = tup_b[:2]

    first_element = tup_a[0] + tup_b[0]
    second_element = tup_a[1] + tup_b[1]

    updated_tup = (first_element, second_element)
    return updated_tup
