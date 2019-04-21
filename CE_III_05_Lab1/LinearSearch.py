# Author : Junth Basnet
# Implementation of Linear Search algorithm

def linear_search(array : list, target: int) -> int :
    for index in range(len(array)):
        if(array[index] == target):
            return index
    return -1