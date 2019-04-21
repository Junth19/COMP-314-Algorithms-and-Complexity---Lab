# Author : Junth Basnet
# Implementation of iterative version of Binary Search algorithm

def iterative_binary_search(array : list , target : int) -> int :
    
    low = 0
    high = len(array) - 1
    
    while (low <= high):
        
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid -1
        else:
            return mid
        
    return -1
