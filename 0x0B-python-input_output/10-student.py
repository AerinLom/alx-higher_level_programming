#!/usr/bin/python3
"""
Defines a class student
"""


class Student:
    """
    Attributes of a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        result = {}
        for attribute in sorted(attrs):
            if hasattr(self, attribute):
                result[attribute] = getattr(self, attribute)
        return result
