#!/usr/bin/python3
'''Module for file storage'''

import json
from os.path import isfile


class FileStorage:
    '''This class does serialization and deserialization to and from Json'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''This methods returns the dictionary __objects'''
        return (self.__objects)

    def new(self, obj):
        '''This methods sets in __objects the obj with a key'''
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        '''This module serialize __objects to the JSON file'''
        serial_obj = {key: ob.to_dict() for key, ob in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serial_obj, file)

    def reload(self):
        '''This module deserializes the JSON file to __objects'''
        from models.base_model import BaseModel
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    deserial_obj = json.load(file)
                    for key, obj_dict in deserial_obj.items():
                        self.__objects[key] = BaseModel(**obj_dict)
                except json.JSONDecodeError:
                    pass
