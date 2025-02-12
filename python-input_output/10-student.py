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
        if isinstance(attrs, list) and all(isinstance(attrs, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
            return self.__dict__
