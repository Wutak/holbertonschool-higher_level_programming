#!/usr/bin/python3
"""class"""


class Square:
    """square"""

    def __init__(self, size=0):
        """init"""
        if not isinstance (size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
