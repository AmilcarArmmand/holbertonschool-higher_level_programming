#!/usr/bin/python3
""" Check for instance of the object """


def is_kind_of_class(obj, a_class):
    """ Return True if same instance of class or False if inherited class """
    return (isinstance(obj, a_class))
