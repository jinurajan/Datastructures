"""
Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
"""

from collections import Counter
from heapq import *
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        min_heap = []
        for value, count in counter.items():
            heappush(min_heap, (count, value))
        
        while k:
            count, value = heappop(min_heap)
            count -= 1
            if count > 0:
                heappush(min_heap, (count, value))    
            k -= 1
        return len(min_heap)

arr = [4,3,1,1,3,3,2]
k = 3
print(Solution().findLeastNumOfUniqueInts(arr, k))