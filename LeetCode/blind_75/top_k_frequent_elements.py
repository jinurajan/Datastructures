"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Input: nums = [1], k = 1
Output: [1]
"""

from collections import Counter
from typing import List
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        min_heap = []
        for num,count in counter.items():
            heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heappop(min_heap)
        result = []
        while min_heap:
            _, num = heappop(min_heap)
            result.append(num)
        return result
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [val[0] for val in counter[:k]]