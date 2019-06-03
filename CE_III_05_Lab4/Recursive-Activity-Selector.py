#Author : Junth Basnet
#Implementation of Activity Selection Problem(Recursive-Version)
#Time Complexity : O(n)

def RecursiveActivitySelector(start, finish, k, n):
    """
    Recursively selects the maximum number of activities from the list of activities
    """

    m = k + 1
    while m < n and start[m] < finish[k] and k >= 0:
        m += 1
    if m < n:
        activity.append(m)
        RecursiveActivitySelector(start, finish, m, n)
    else:
        return None
    return activity
        


#List to store the activities
activity = []

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
MaximumActivity = RecursiveActivitySelector(start, finish, -1, len(finish))
print(MaximumActivity)
