import unittest
from flask import json
import sys
sys.path.append('..')
import reilly as main

'''
Opens JSON file with test inputs
'''
def get_data(filename):
    fd = open(filename)
    data = json.load(fd)
    fd.close()
    return data

class TestCreateIndexJSON(unittest.TestCase):
    '''
    Testing creation of JSON to be sent to Indexing
    '''

    def test_empty_query(self):
        '''
        Empty query to be sent to indexing
        '''
        data = get_data('query-empty.json')
        index_json = main.create_indexing_json(data)
        self.assertEqual(len(index_json['tokens']), 0)


    def test_one_word(self):
        '''
        One word query
        '''
        data = get_data('query-one-word.json')
        index_json = main.create_indexing_json(data)
        self.assertEqual(len(index_json['tokens']), 1)
        self.assertEqual(index_json['tokens'][0], 'food')
        
    def test_two_words(self):
        '''
        Two word query
        '''
        data = get_data('query-two-words.json')
        index_json = main.create_indexing_json(data)
        self.assertEqual(len(index_json['tokens']), 2)
        self.assertEqual(index_json['tokens'][0], 'eating')
        self.assertEqual(index_json['tokens'][1], 'healthy')


    def test_three_words(self):
        '''
        Three word query
        '''
        data = get_data('query-three-words.json')
        index_json = main.create_indexing_json(data)
        self.assertEqual(len(index_json['tokens']), 3)
        self.assertEqual(index_json['tokens'][0], 'eating')
        self.assertEqual(index_json['tokens'][1], 'healthy')
        self.assertEqual(index_json['tokens'][2], 'food')


if __name__ == '__main__':
    unittest.main()
