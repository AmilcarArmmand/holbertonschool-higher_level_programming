#!/usr/bin/python3
""" A function that returns a list of available attributes and methods """


def lookup(obj):
    """ Returns list of attributes and methods """
    return (dir(obj))
