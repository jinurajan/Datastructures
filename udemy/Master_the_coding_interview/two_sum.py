"""
you are given an array and a target value
return the indices of the values if the sum of the values == target
"""


def two_sum(array, target):
    # brute force
    # T = O(N*N)
    # S = 0
    for i, n in enumerate(array):
        T = target - n
        for j in range(i+1, len(array)):
            if array[j] == T:
                return [i, j]

def two_sum(array, target):
    """optimized
    T = O(N)
    S = O(N)
    """
    map = {}
    for i, n in enumerate(array):
        T = target - n
        if T in map:
            return [map[T], i]
        map[n] = i