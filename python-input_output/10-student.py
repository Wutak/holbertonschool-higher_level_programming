#!/usr/bin/python3
"""json"""


class Student:
    """json"""

    def __init__(self, first_name, last_name, age):
        """json"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        if attrs is None:
            return vars(self)
        else:
            mydict = {}
            for i in attrs:
                if hasattr(self, i):
                    mydict[i] = getattr(self, i)
        return mydict
