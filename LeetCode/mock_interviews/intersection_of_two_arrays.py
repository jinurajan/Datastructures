"""
Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

from typing import List
from collections import defaultdict


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        hash_map = defaultdict(list)
        for idx, n in enumerate(nums1):
            hash_map[n].append(idx)
        res = []
        for n in nums2:
            if n not in hash_map or not hash_map[n]:
                continue
            hash_map[n].pop()
            res.append(n)
        return res

nums1=[1,2]
nums2=[1,1]
print(Solution().intersect(nums1, nums2))
nums1= [4,7,9,7,6,7]
nums2 = [5,0,0,6,1,6,2,2,4]
print(Solution().intersect(nums1, nums2))
