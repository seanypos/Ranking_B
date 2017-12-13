import unittest
from flask import json
import sys
sys.path.append('..')
import simulation as main

EPSILON = 1e-3

'''
Opens JSON file with test inputs
'''
def get_data(filename):
    fd = open(filename)
    data = json.load(fd)
    fd.close()
    return data

'''
Test case helper function to load in test indexing and link analysis data
'''
def load_data(index_file, link_anal_file):
    indexing = get_data(index_file)
    link_analysis = get_data(link_anal_file)
    weights, urls = main.create_dict(indexing)
    weights = main.add_weight(indexing, link_analysis, urls, weights)
    return weights

class TestAddWeight(unittest.TestCase):
    '''
    Testing Add Weight Function
    '''

    def test_no_links(self):
        '''
        No webpages
        '''
        weights = load_data('index-nolinks.json', 'la-nolinks.json')
        self.assertEqual(len(weights), 0)

    def test_one_link(self):
        '''
        One webpage
        '''
        weights = load_data('index-onelink.json', 'la-onelink.json')
        self.assertEqual(len(weights), 1)
        self.assertLessEqual(weights['eathealthy.com'] - .6, EPSILON)

    def test_average_links(self):
        '''
        Average case
        '''
        weights = load_data('index-average.json', 'la-average.json')
        self.assertEqual(len(weights), 10)
        self.assertLessEqual(weights['nutritionfacts.com'] - 2.6, EPSILON)
        self.assertLessEqual(weights['webmd/nutritionfacts.com'] - 2.8, EPSILON)
        self.assertLessEqual(weights['eatinghealthy.com'] - 3.0, EPSILON)
        self.assertLessEqual(weights['weightwatchers.com'] - 3.2, EPSILON)
        self.assertLessEqual(weights['cleaneating.com'] - 3.4, EPSILON)
        self.assertLessEqual(weights['lifestyle.com'] - 3.6, EPSILON)
        self.assertLessEqual(weights['healthy.com'] - 3.8, EPSILON)
        self.assertLessEqual(weights['wickedhealthy.com'] - 4.0, EPSILON)
        self.assertLessEqual(weights['eatgood.com'] - 4.2, EPSILON)
        self.assertLessEqual(weights['befit.com'] - 4.4, EPSILON)

if __name__ == '__main__':
    unittest.main()
