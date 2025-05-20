#!/usr/bin/python3
"""class"""


class Square:
    """square"""

    def __init__(self, size=0):
        """init"""
        self.size = size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area"""
        return self._size**2

    def my_print(self):
        """print"""
        if size == 0:
            print("")
        else:
            for i in range(self.size):
                print(self.size * "#")

    @property
    def position(self):
        """position"""
        return self.__position

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
            return self.__size**2

        def  my_print(self):
            """print"""
            if self.__size == 0:
                print()
                return
            for i in range(self.__position[1]):
                print()
            for i in range(self.__position[0]):
                print(" " * self.__position[0] + "#" * self.__size)
