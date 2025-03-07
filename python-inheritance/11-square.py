#!/usr/bin/python3
"""write a classe square inheriting from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inheriting from rectangle"""

    def __init__(self, size):
        """instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area() method"""
        return self.__size ** 2

    def __str__(self):
        """prints square's description"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
