#!/usr/bin/python3
"""
Square: Class that defines a square
"""


class Square:
    """ Class object """
    def __init__(self, size=0):
        """ Method to create a new instance of a class object

        Args:
            size (int): The size of the new square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
