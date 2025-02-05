#!/usr/bin/python3
"""write class basegeometry"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method"""
        if type(value) is not int:
            raise TypeError("[] must be an integer".format(name))

        if value <= 0:
            raise ValueError("[] mus tbe greater than 0".format(name))
