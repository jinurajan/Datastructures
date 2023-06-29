"""
Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        n = len(height)
        left = 0
        right = n-1
        while left < right:
            min_height = min(height[left], height[right])
            max_amount = max(max_amount, min_height * (right-left))
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return max_amount
        