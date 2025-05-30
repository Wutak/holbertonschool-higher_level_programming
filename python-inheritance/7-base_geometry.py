#!/usr/bin/python3
"""geometry"""


class BaseGeometry():
    """class"""

    def __init__(self):
        """init"""
        pass

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if not isinstance(value, int):
            raise TypeError("{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than 0")
