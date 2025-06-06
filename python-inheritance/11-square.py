#!/usr/bin/python3
"""square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return "Square {}/{}".format(self.__width, self.__height)
