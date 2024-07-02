#!/usr/bin/python3
"""11. Student to disk and reload"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        to_json_dict = {}

        if attrs is None:
            to_json_dict = self.__dict__
        else:
            for attr in attrs:
                if attr in self.__dict__:
                    to_json_dict[attr] = self.__dict__[attr]

        return to_json_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if json:
            self.first_name = json['first_name']
            self.last_name = json['last_name']
            self.age = json['age']
