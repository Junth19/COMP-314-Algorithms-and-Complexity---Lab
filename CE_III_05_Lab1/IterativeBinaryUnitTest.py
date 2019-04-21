#Author : Junth Basnet

import unittest
from IterativeBinarySearch import iterative_binary_search


class TestSearch(unittest.TestCase):
    
    #Unit test for Iterative version of Binary Search
    def test_iterative_binary_search(self):
        
        array = list(range(10))
        
        #Test for element that are in list
        self.assertEqual(iterative_binary_search(array, 0), 0)
        self.assertEqual(iterative_binary_search(array, 1), 1)
        self.assertEqual(iterative_binary_search(array, 2), 2)
        self.assertEqual(iterative_binary_search(array, 3), 3)
        self.assertEqual(iterative_binary_search(array, 4), 4)
        self.assertEqual(iterative_binary_search(array, 5), 5)
        self.assertEqual(iterative_binary_search(array, 6), 6)
        self.assertEqual(iterative_binary_search(array, 7), 7)
        self.assertEqual(iterative_binary_search(array, 8), 8)
        self.assertEqual(iterative_binary_search(array, 9), 9)
        
        

        #Test for element that are not in the list
        self.assertEqual(iterative_binary_search(array, 10), -1)
        self.assertEqual(iterative_binary_search(array, 11), -1)
        

if __name__ == "__main__":
    unittest.main()
        
