#!/usr/bin/python3


"""A function that returns the list of available attributes and methods of an object"""
def lookup(obj):
    list_methods = dir(obj)
    
    """ Returns the list of available attributes and methods of an object"""
    return list_methods
