#!/usr/bin/python3
""" Define a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectanlge class. """

    def __init__(self, width, height):
        """ Create instance of a rectange """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Method that calculates area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Method to return rectangle description """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
