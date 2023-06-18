"""
"""
from typing import List


class Solution:
    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        result = []
        n = len(nums)
        # input is sorted
        for i in range(k-1, n):
            result.append(nums[i-(k-1)])
        return result


nums = [1,2,3,4,5,6,7,8,9]
print(Solution().minSlidingWindow(nums, 4))
print(Solution().minSlidingWindow(nums, 3))
