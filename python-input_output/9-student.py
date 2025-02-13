#!/usr/bin/python3
"""json"""


class Student:
    """json"""

    def __init__(self, first_name, last_name, age):
    """json"""

    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self):
        """json"""
        return vars(self)
