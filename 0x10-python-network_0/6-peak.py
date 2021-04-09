""" Function that finds the peak in a list of numbers """


def find_peak(list_of_integers):
    """Find peak in unsorted list of numbers"""
    if len(list_of_integers).__eq__(0):
        return None
    if len(list_of_integers).__eq__(1):
        return list_of_integers[0]
