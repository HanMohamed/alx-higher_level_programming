#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""

        return Student.___dict__
