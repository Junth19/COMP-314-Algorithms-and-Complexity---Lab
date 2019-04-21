# Author : Junth Basnet
# Implementation of recursive version of Binary Search algorithm

def recursive_binary_search(array : list, target : int, low : int, high : int) -> int :
    if low <= high :
        mid = (low + high) // 2
        if array[mid] < target :
            return recursive_binary_search(array, target, mid + 1, high)
        elif array[mid] > target :
            return recursive_binary_search(array, target, low, mid - 1)
        else:
            return mid
    return -1
