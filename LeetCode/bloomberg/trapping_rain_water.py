"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        max_left = 0
        max_right = 0
        left = 0
        right = n-1
        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                max_area += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                max_area += max_right - height[right]
                right -= 1
        return max_area
    

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height=height))