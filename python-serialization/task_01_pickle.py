#!/usr/bin/env python3
"""pickle"""


import pickle


class CustomObject:
    """class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                filename = pickle.dump(self, file)
            return filename
            
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return (pickle.load(file.read()))
        except Exception:
            return None
