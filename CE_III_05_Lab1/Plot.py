#Author : Junth Basnet

import time
import random
import matplotlib.pyplot as plt
from LinearSearch import linear_search
from RecursiveBinarySearch import recursive_binary_search
from IterativeBinarySearch import iterative_binary_search

def plot_linear_search() -> None :
        random_size = random.randint(1,10000)
        sorted_array = sorted(random.sample(range(10000), random_size))
        execution_time = list()
        target = random.choice(sorted_array)
        
        for i in range(10000, 100001, 10000):
            start_time = time.time()
            index = linear_search(sorted_array, target)
            end_time = time.time()
            execution_time.append(end_time - start_time)
        print(execution_time)
        plt.plot(execution_time, color = 'red', lw = 10)
        plt.xlabel('Input-Size(n)')
        plt.ylabel('Execution-Time(t)')
        plt.show()

def plot_iterative_binary_search() -> None :
        random_size = random.randint(1,10000)
        sorted_array = sorted(random.sample(range(10000), random_size))
        execution_time = list()
        target = random.choice(sorted_array)
        
        for i in range(10000, 100001, 10000):
            start_time = time.time()
            index = iterative_binary_search(sorted_array, target)
            end_time = time.time()
            execution_time.append(end_time - start_time)
        print(execution_time)
        plt.plot(execution_time, color = 'red', lw = 10)
        plt.xlabel('Input-Size(n)')
        plt.ylabel('Execution-Time(t)')
        plt.show()

def plot_recursive_binary_search() -> None :
        random_size = random.randint(1,10000)
        sorted_array = sorted(random.sample(range(10000), random_size))
        execution_time = list()
        target = random.choice(sorted_array)
        
        for i in range(10000, 100001, 10000):
            start_time = time.time()
            index = recursive_binary_search(sorted_array, target, 0, random_size - 1)
            end_time = time.time()
            execution_time.append(end_time - start_time)
        print(execution_time)
        plt.plot(execution_time, color = 'red', lw = 10)
        plt.xlabel('Input-Size(n)')
        plt.ylabel('Execution-Time(t)')
        plt.show()


            
        
        

if __name__ == "__main__":
    plot_linear_search()
    plot_iterative_binary_search()
    plot_recursive_binary_search()
        

    

