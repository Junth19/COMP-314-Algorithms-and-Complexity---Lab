# Author : Junth Basnet
#Implementation of merge sort

def merge_sort(array, p, r):
    
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r )
        merge(array, p, q, r)

def merge(array, p, mid, r):

    left_array = array[:mid]
    right_array = array[mid:]
    
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i = i + 1
        else:
            array[k] = right_array[j]
            j = j + 1
        k = k + 1

    while i < len(left_array):
        array[k] = left_array[i]
        i = i + 1
        k = k + 1

    while j < len(right_array):
        array[k] = right_array[j]
        j = j + 1
        k = k + 1
    
array = [54,26,93,17,77,31,44,55,20]
merge_sort(array, 0, len(array) - 1)
print(array)
