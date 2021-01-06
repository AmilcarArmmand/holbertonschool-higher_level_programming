#!/usr/bin/python3
"""
Square: Class that defines a square
"""


class Square:
    """ Class object """
    def __init__(self, size=0, position=(0, 0)):
        """ Method to create a new instance of a class object

        Args:
            size (int): The size of the new square
            position (int, int): The position of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Get current position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Set the position of the square """
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)
        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message)
        self.__position = value

    def area(self):
        """ Method that returns the area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ Print the square in sdtout with the # character """
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            print("#" * self.__size)
