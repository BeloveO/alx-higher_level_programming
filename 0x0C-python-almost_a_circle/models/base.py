#!/usr/bin/python3
"""
class Base to be the base of all other classes
"""
import json
import os.path
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        file = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(file, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        file = "{}.csv".format(cls.__name__)

        if os.path.exists(file) is False:
            return []

        with open(file, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        pass
