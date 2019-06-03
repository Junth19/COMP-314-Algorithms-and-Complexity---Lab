#Author : Junth Basnet
#Implementation of Activity Selection Problem(Iterative-Version)
#Time Complexity : O(n)

def GreedyActivitySelector(start, finish):
    """
    Selects maximum number of activities from the list of activities
    """

    #First activity is always selected
    activity = [0]
    i = 0
    for m in range(1,len(finish)):
        if start[m] >= finish[i]:
            activity.append(m)
            i = m
    print(activity)

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
finish_sorted = sorted(zip(finish, start))
#print(finish_sorted)
finish, start = list(zip(*finish_sorted))

GreedyActivitySelector(start, finish)