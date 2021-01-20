#!/usr/bin/python3
""" Defile a class BaseGeometry """


class BaseGeometry:
    """ Base class of geometry. """
    def area(self):
        """ No implemented method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
