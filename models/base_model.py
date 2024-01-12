#!/usr/bin/python3
'''Base Model Module for the Base's model of all others project's object'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    Basemodel class defines all common attributes and methods for other cls
    '''
    def __init__(self, *args, **kwargs):
        '''Init method for Base Model'''
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            d_format = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(kwargs['created_at'], d_format)
            self.updated_at = datetime.strptime(kwargs['updated_at'], d_format)

            for key, value in kwargs.items():
                if key != '__class__' and key != 'created_at' and \
                   key != 'updated_at':
                    setattr(self, key, value)

    def __str__(self):
        '''string representation for my Base model class'''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''method for updates date and time'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Methods that returns a dictionary containing all keys/values
        of __dict__ of the instance and the class name with key __class__
        '''
        my_dict_model = self.__dict__.copy()
        my_dict_model['__class__'] = self.__class__.__name__
        my_dict_model['created_at'] = self.created_at.isoformat()
        my_dict_model['updated_at'] = self.updated_at.isoformat()
        return (my_dict_model)
