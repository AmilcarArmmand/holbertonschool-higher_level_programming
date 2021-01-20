#!/usr/bin/python3
""" Check Only sub class of object """


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of a subclass """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
