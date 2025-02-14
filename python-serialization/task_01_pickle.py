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
        except Exception as exc:
            print(f"Error serializing object: {exc}")

    def deserialize(cls, filename):
        """pickle"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as exc:
            print(f"Error deserializing object: {exc}")
            return None
