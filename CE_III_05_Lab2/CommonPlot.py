#Author : Junth Basnet
#Plot module for Sorting algorithm(Insertion Sort and Merge Sort)

import matplotlib.pyplot as plt

def plot_sorting_algorithm(execution_time):
    
    time_to_execute = list(execution_time.values())
    input_size = list(execution_time.keys())

    plt.plot(input_size, time_to_execute)
    plt.xlabel('Input-Size(n)')
    plt.ylabel('Execution Time (sec)')
    plt.xticks(input_size)
    plt.yticks(time_to_execute)
    plt.show()
