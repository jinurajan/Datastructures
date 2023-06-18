"""
Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

1. sliding window ? 
"""
from typing import List
from collections import Counter


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total_count = 0
        count = 0
        start = 0
        end = 0
        freq = Counter()
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        while end < n:
            count += nums[end]
            if count == k:
                total_count += 1
            total_count += freq[count-k]
            freq[count] += 1
            end += 1
        return total_count




class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0

        result = 0
        i = 0
        count = 0
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
                count = 0
            
            while odd_count == k:
                if nums[i] %2 == 1:
                    odd_count -= 1
                i += 1
                count += 1
            
            result += count
        return result