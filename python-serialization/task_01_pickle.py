#!/usr/bin/python3
"""pickle"""


import pickle


class CustomObject:
    """pickle"""

    def __init__(self, name, age, is_student)
        """pickle"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """pickle"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return filename
        except:
            return None

    def deserialize(cls, filename):
        """pickle"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
            return data
        except:
            return None
