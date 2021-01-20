#!/usr/bin/python3
""" Check for same instance of object """


def is_same_class(obj, a_class):
    """ Returns True is object is exactly an instance of specified class """
    return (type(obj) is (a_class))
