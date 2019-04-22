#Author : Junth Basnet

import time
import random
from LinearSearch import linear_search
from RecursiveBinarySearch import recursive_binary_search
from IterativeBinarySearch import iterative_binary_search

def random_test() -> None :
    for i in range(2000):
        random_size = random.randint(1,50)
        sorted_array = sorted(random.sample(range(10000), random_size))

        #Choose random element from array
        target = random.choice(sorted_array)
        #find actual index of target element
        actual_index = sorted_array.index(target)


        assert(linear_search(sorted_array,target) == actual_index )
        assert(iterative_binary_search(sorted_array, target) == actual_index )
        assert(recursive_binary_search(sorted_array, target, 0, random_size - 1) == actual_index )

        print('Testcase {} passed'.format(i+1))


if __name__ == "__main__":
    random_test()
        

    

