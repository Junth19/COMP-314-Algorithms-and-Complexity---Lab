#Author : Junth Basnet
#unit test to check whether merge sort is working properly

import unittest
from MergeSort import merge_sort

class TestSearch(unittest.TestCase):
    
    def test_merge_sort(self):

        
        array_1 = [1, 5, 3, 2, 4]
        merge_sort(array_1, 0, len(array_1))
        self.assertListEqual(array_1, [1, 2, 3, 4, 5])

        array_2 = [1, 6, 5, 2, 4]
        merge_sort(array_2, 0, len(array_2))
        self.assertListEqual(array_2, [1, 2, 4, 5, 6])

        array_3 = [1, 6, 5, 2, 10, 4]
        merge_sort(array_3, 0, len(array_3))
        self.assertListEqual(array_3, [1, 2, 4, 5, 6, 10])

        array_4 = [1, 5, 3, 2, 4, 5, 6, 25]
        merge_sort(array_4, 0, len(array_4))
        self.assertListEqual(array_4, [1, 2, 3, 4, 5, 5, 6, 25] )
        

if __name__ == "__main__":
    unittest.main()
