"""
Given an array of integers arr and an integer k, return the k most frequent elements.
"""

from heapq import heappush, heappop
from collections import Counter
def top_k_frequent(arr, k):
    counter = Counter(arr)
    min_heap = []
    for key, freq in counter.items():
        heappush(min_heap, (freq, key))
        if len(min_heap) > k:
            heappop(min_heap)
        
    result = []
    while min_heap:
        _, val = heappop(min_heap)
        result.append(val)
    return result



# Driver code
def main():
    arr = [[1, 3, 5, 12, 11, 12, 11, 12, 5], [1, 3, 5, 14, 18, 14, 5],
           [2, 3, 4, 5, 6, 7, 7], [9, 8, 7, 6, 5, 4, 3, 2, 1], 
           [2, 4, 3, 2, 3, 4, 5, 4, 4, 4], [1, 1, 1, 1, 1, 1], [2, 3]]
    k = [3, 2, 1, 1, 3, 1, 2]

    for i in range(len(k)):
        print(i+1, ". \t Input: (", arr[i], ", ", k[i], ")", sep="")
        print("\t Top", k[i], "frequent Elements: ",
              top_k_frequent(arr[i], k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()