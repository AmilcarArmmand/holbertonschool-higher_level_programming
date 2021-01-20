#!/usr/bin/python3
""" Function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ Returns number of characters appended to the end of file """
    with open(filename, 'a+', encoding='utf-8') as myfile:
        return myfile.write(text)
