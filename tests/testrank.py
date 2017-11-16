import unittest

def rank(uris):
    return uris

class TestRank(unittest.TestCase):
    '''
    Test the rank function
    '''

    def test_rank_no_links(self):
        '''
        Test that the ranking of zero links returns zero links
        '''
        result = rank([])
        self.assertEqual(result, [])

    def test_rank_one_link(self):
        '''
        Test that the ranking of one link returns the correct result
        '''
        result = rank(['uri'])
        self.assertEqual(result, ['uri'])

if __name__ == '__main__':
    unittest.main()
