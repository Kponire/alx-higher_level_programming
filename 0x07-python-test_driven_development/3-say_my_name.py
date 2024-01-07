#!/usr/bin/python3
"""
module that print Names
"""


def say_my_name(first_name, last_name=""):
    """
        print name and last name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
