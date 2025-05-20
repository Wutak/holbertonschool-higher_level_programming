#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """class"""

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def  height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
