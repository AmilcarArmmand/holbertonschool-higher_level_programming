#!/usr/bin/python3
""" Write string to text file (UTF-8) and returns number of chars printed """


def write_file(filename="", text=""):
    """ Write to a file in UTF-8 format return characters written """
    with open(filename, 'w', encoding='utf-8') as myfile:
        myfile.write(text)
        return myfile.write(text)
