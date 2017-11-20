import unittest
from flask import json

import sys
sys.path.append('..')
import api

class TestIndexing(unittest.TestCase):
    '''
    Test indexing API
    '''

    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()
    
    def test_index_no_links(self):
        # Read json from file
        fd = open('nolinks-index-output.json')
        data = json.load(fd)
        fd.close()

        # Send POST request
        response = self.app.post('/sendquery/1', data=json.dumps(data), content_type='application/json')

    def test_index_one_link(self):
        fd = open('oneline-index-output.json')
        data = json.load(fd)
        fd.close()

        # Send POST request
        response = self.app.post('/sendquery/1', data=json.dumps(data), content_type='application/json')
        


if __name__ == '__main__':
    unittest.main()
