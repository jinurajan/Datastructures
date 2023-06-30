"""
Number of Subsequences That Satisfy the Given Sum Condition


You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)


"""
from typing import List
import bisect

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = pow(10, 9) + 7
        nums.sort()
        result = 0

        for left in range(n):
            # find the position the right with a diff from target- starting value 
            right = bisect.bisect_right(nums, target-nums[left]) - 1
            if right >= left:
                # 2 to the pow of the length of the subsequence
                result += pow(2, right-left, mod)
        return result % mod


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = pow(10, 9) + 7
        nums.sort()
        result = 0

        left = 0
        right = n-1
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + pow(2, right-left, mod)) % mod
                left += 1
            else:
                right -= 1
        return result

