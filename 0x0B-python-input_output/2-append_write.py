#!/usr/bin/python3
"""   """


def append_write(filename="", text=""):
    """   """
    with open(filename, 'a', encoding='utf-8') as myfile:
        return myfile.write(text)
