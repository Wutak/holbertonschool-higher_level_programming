#!/usr/bin/python3
"""rectangle"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """class"""

    def __init__(self, width, height):
        """init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def __str__(self):
        """str"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height)
