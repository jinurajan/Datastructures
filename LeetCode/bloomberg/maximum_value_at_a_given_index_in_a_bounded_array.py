"""
Maximum Value at a Given Index in a Bounded Array

You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.
"""

class Solution:
    def get_sum(self, index:int, value:int, n:int) -> int:
        count = 0
        """
        on indexs left
        if value > index there are index+1 numbers in AP
        [value-index, ..., value-1, value]
        else 
        [1, 2, .. value-1, value] plus a sequence of length index-value+1
        """
        if value > index:
            count += (value + value-index) * (index+1) // 2
        else:
            count += (value+1) * value // 2 + index - value + 1
        """
        if value >= n-index there are n-index numbers in the AP
        [value, value-1, .... value-n+1+index]
        else[value, value-1, ..... 1] plus sequence of length n-index-value
        """
        if value >= n-index:
            count += (value + value-n+1+index) * (n-index) // 2
        else:
            count += (value+1)* value // 2 + n-index-value
        
        return count- value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left+right+1) // 2
            if self.get_sum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid-1
        return left
            