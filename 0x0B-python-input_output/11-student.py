#!/usr/bin/python3
"""
class Student
"""


class Student():
    """
    Class to create student instances
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dict representation of the student
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the student instance
        """
        for attri in json:
            self.__dict__[attri] = json[attri]
