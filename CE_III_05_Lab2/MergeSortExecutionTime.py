#Author : Junth Basnet
# Calculating execution time of merge sort

import random
import time
from MergeSort import merge_sort
from CommonPlot import plot_sorting_algorithm

def merge_sort_time():

    #Create empty dictionary
    execution_time = {}

    for i in range(500,1001,500):
        
        try:
            unsorted_array = (random.sample(range(i), i))
        except ValueError:
            print("Sample larger than population or is negative")
            
        start_time = time.time()
        merge_sort(unsorted_array, 0, len(unsorted_array))
        end_time = time.time()
        
        #Input size and its corresponding execution time is added to dictionary
        execution_time[i] = end_time - start_time
        
    print(execution_time)
    plot_sorting_algorithm(execution_time)
    
if __name__ == "__main__":
    merge_sort_time()
    
