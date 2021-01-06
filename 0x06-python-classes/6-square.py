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

    @property
    def size(self):
        """ get the current size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the current size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method that returns the area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ Print the square in sdtout with the # character """
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            print("#" * self.__size)
