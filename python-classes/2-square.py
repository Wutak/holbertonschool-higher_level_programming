#!/usr/bin/python3
"""program that creates the class Square with attribute size"""


class Square:
    """size must be an int and greater than 0"""

    def __init__(self, size=0):
        """optional initialization with size, verify value and type"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
