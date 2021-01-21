#!/usr/bin/python3
""" function writes an Object to a text file, using a JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ Writes JSON to file"""
    with open(filename, 'w', encoding='utf-8') as myfile:
        json.dumps(my_obj, myfile)
