"""
Largest Rectangle in Histogram


Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)
        for idx, height in enumerate(heights):
            if stack and height == stack[-1][1]:
                continue
            min_start_idx = idx
            while stack and height < stack[-1][1]:
                start_idx, last_height = stack.pop()
                min_start_idx = start_idx
                max_area = max(max_area, last_height*(idx-start_idx))
            stack.append((min_start_idx, height))
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]
        n = len(heights)
        for idx in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[idx]:
                curr_height = heights[stack.pop()]
                current_width = idx - stack[-1] - 1
                max_area = max(max_area, curr_height * current_width)
            stack.append(idx)
        
        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            current_width = n - stack[-1]-1
            max_area = max(max_area, curr_height * current_width)
        
        return max_area