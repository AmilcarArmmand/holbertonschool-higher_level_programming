#!/usr/bin/python3
""" Function that reads a text file in UTF-8 and prints to stdout """


def read_file(filename=""):
    """ Print file to stdout """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
