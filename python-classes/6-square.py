#!/usr/bin/python3
"""program thar creates the class Square that defines a square"""


class Square:
    """defines a square by its size"""

    def __init__(self, size=0):
        """optional initialization with private attrivute size, an int >= 0"""
        self._size = size

    @property
    def size(self):
        """method to retrieve size value"""
        return size

    @size.setter
    def size(self, value):
        """method to set size value"""
        if type(size) is not int:
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """returns area of the square"""
        return (self._size**2)
    
    def my_print(self):
        """method that prints a square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * "#")
