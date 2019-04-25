#Author : Junth Basnet
#Implementation of insertion sort

def insertion_sort(array : list) -> list :
    for i in range(1,len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value :
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = value
    return array
#result = insertion_sort([1,5,3,2,4])
#print(result)
