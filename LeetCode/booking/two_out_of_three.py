"""
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 

"""
from typing import List
from collections import defaultdict


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums3) & set(nums1)


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        occupancy = defaultdict(set)
        for num in nums1:
            occupancy[num].add(1)
        for num in nums2:
            occupancy[num].add(2)
        for num in nums3:
            occupancy[num].add(3)
        
        result = []
        for key, value in occupancy.items():
            if len(value) >= 2:
                result.append(key)
        return result     
