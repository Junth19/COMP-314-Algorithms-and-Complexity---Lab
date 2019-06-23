#Author : Junth Basnet

import unittest
from Greedy_Activity_Selector import GreedyActivitySelector
from Recursive_Activity_Selector import RecursiveActivitySelector

class GreedyAlgorithm(unittest.TestCase):
    
    def activity_selector_test(self):

        self.assertListEqual(GreedyActivitySelector([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 10]), [0, 1, 3, 4])           
        self.assertListEqual(RecursiveActivitySelector([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9], -1, 6), [0, 1, 3, 4])

        self.assertListEqual(GreedyActivitySelector([1, 5, 6, 7, 4, 8], [2, 8, 5, 3, 6, 7]), [0, 1, 5])
        self.assertListEqual(RecursionActivitySelector([1, 5, 6, 7, 4, 8], [2, 8, 5, 3, 6, 7], -1, 6), [0, 1, 5])           
        

if __name__ == "__main__":
    unittest.main()
