# Author : Junth Basnet

import unittest
from RecursiveBinarySearch import recursive_binary_search


class TestSearch(unittest.TestCase):
    
    #Unit test for Recursive Version of Binary Search
    def test_recursive_binary_search(self):
        
        array = list(range(10))
        
        self.assertEqual(recursive_binary_search(array, 0, 0, len(array)), 0)
        self.assertEqual(recursive_binary_search(array, 1, 0, len(array)), 1)
        self.assertEqual(recursive_binary_search(array, 2, 0, len(array)), 2)
        self.assertEqual(recursive_binary_search(array, 3, 0, len(array)), 3)
        self.assertEqual(recursive_binary_search(array, 4, 0, len(array)), 4)
        self.assertEqual(recursive_binary_search(array, 5, 0, len(array)), 5)
        self.assertEqual(recursive_binary_search(array, 6, 0, len(array)), 6)
        self.assertEqual(recursive_binary_search(array, 7, 0, len(array)), 7)
        self.assertEqual(recursive_binary_search(array, 8, 0, len(array)), 8)
        self.assertEqual(recursive_binary_search(array, 9, 0, len(array)), 9)
        
if __name__ == "__main__":
    unittest.main()
        
