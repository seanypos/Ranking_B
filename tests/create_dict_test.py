import unittest
from flask import json
import sys
sys.path.append('..')
import simulation as main

'''
Opens JSON file with test inputs
'''
def get_data(filename):
    fd = open(filename)
    data = json.load(fd)
    fd.close()
    return data

class TestCreateDict(unittest.TestCase):
    '''
    Testing creations of weight dictionary
    '''
    
    def test_no_links(self):
        '''
        No links in json
        '''
        data = get_data('index-nolinks.json')
        weights, urls = main.create_dict(data)
        
        self.assertEqual(len(urls), 0)
        self.assertEqual(len(weights), 0)

        
    def test_one_link(self):
        '''
        One link in json
        '''
        data = get_data('index-onelink.json')
        weights, urls = main.create_dict(data)

        self.assertEqual(len(urls), 1)
        self.assertEqual(len(weights), 1)
        self.assertEqual(weights['eathealthy.com'], 0)

        
    def test_average(self):
        '''
        Average response
        '''
        data = get_data('index-average.json')
        weights, urls = main.create_dict(data)

        self.assertEqual(len(urls), 10)
        self.assertEqual(len(weights), 10)
        for url in weights.keys():
            self.assertEqual(weights[url], 0)

    
        
if __name__ == '__main__':
    unittest.main()
