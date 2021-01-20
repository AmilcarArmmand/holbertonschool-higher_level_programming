#!/usr/bin/python3
""" Class MyList that inherits from list """


class MyList(list):
    """ Class that inherits from list """

    def print_sorted(self):
        """ Public instance method that prints sorted list """
        print(sorted(self))
