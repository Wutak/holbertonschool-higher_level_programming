#!/usr/bin/python3
"""class"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i,  int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def area(self):
        """area"""
        return self.__size ** 2

    def my_print(self):
        """print"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
