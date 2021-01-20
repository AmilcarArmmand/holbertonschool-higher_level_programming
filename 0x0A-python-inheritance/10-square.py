#!/usr/bin/python3
""" Class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The square class """

    def __init__(self, size):
        """ Create instance """
        super().__init__(size, size)
        self.__size = size
