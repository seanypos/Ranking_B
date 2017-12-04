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

class TestCreateLinkJson(unittest.TestCase):
    '''
    Testing creating of JSON to be sent to Link Analysis
    '''

    def test_no_links(self):
        '''
        No links to be sent to link analysis
        '''
        data = get_data('index-nolinks.json')
        weights, urls = main.create_dict(data)
        la_json = json.loads(main.create_link_json(urls))
        self.assertEqual(len(la_json["webpages"]), 0)

        
    def test_one_link(self):
        '''
        One link to be sent to link analysis
        '''
        data = get_data('index-onelink.json')
        weights, urls = main.create_dict(data)
        la_json = json.loads(main.create_link_json(urls))
        self.assertEqual(len(la_json["webpages"]), 1)

    def test_average(self):
        '''
        Typical number of links to be sent to link analysis
        '''
        data = get_data('index-average.json')
        weights, urls = main.create_dict(data)
        la_json = json.loads(main.create_link_json(urls))
        self.assertEqual(len(la_json["webpages"]), 10)

if __name__ == '__main__':
    unittest.main()
