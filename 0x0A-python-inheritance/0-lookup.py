#!/usr/bin/python3

def lookup(obj):
    list_methods = dir(obj)
    
    """ Returns the list of available attributes and methods of an object"""
    return list_methods
