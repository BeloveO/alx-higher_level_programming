#!/usr/bin/python3
"""
class Base to be the base of all other classes
"""
import json
import os.path


class Base:
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        List to JSON string
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string rep to a file
        """
        file = "{}.json".format(cls.__name__)
        list_dic = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(list_dic)
        with open(file, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
        JSON string to dictionary
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        file = "{}.json".format(cls.__name__)

        if os.path.exists(file) is False:
            return []

        with open(file, 'r') as f:
            str_list = f.read()

        list_cls = cls.from_json_string(str_list)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))
        return list_ins
