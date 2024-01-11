'''Unittest module for BaseModel'''
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''Test class for Base Model'''
    def setUp(self):
        '''Setting up of tests'''
        self.bmodel_inst = BaseModel()

    def test_inst_attr(self):
        '''Method to test attributes'''
        self.assertTrue(hasattr(self.bmodel_inst, 'id'))
        self.assertTrue(hasattr(self.bmodel_inst, 'created_at'))
        self.assertTrue(hasattr(self.bmodel_inst, 'updated_at'))

    def test_save(self):
        '''Method for testing save method'''
        prev_updt = self.bmodel_inst.updated_at
        self.bmodel_inst.save()
        self.assertNotEqual(prev_updt, self.bmodel_inst.updated_at)

    def test_to_dict(self):
        '''Method for testing to_dict method'''
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        bmodel_dict = self.bmodel_inst.to_dict()
        for key in expected_keys:
            self.assertIn(key, bmodel_dict)

    def test_str_method(self):
        '''Method to test str method'''
        str_repr = str(self.bmodel_inst)
        self.assertTrue(str_repr.startswith('[BaseModel]'))
        self.assertIn(self.bmodel_inst.id, str_repr)
        self.assertIn(str(self.bmodel_inst.__dict__), str_repr)


if __name__ == '__main__':
    unittest.main()
