#Author : Junth Basnet
#unit test to check whether insertion sort is working properly

import unittest
from InsertionSort import insertion_sort

class TestSearch(unittest.TestCase):
    
    def test_insertion_sort(self):
        
        self.assertListEqual(insertion_sort([1,5,3,2,4]), [1,2,3,4,5])
        self.assertListEqual(insertion_sort([8,5,3,2,4]), [2,3,4,5,8])
        self.assertListEqual(insertion_sort([1,5,25,2,4]), [1,2,4,5,25])
        self.assertListEqual(insertion_sort([1,5,9,3,2,4]), [1,2,3,4,5,9])
        self.assertListEqual(insertion_sort([1,5,3,2,100,4]), [1,2,3,4,5,100])

if __name__ == "__main__":
    unittest.main()
