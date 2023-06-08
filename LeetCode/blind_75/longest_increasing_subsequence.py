"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


Thoughts

1. subsequence not subarray ie does not need to be contigous
2. bruteforce - O(n2)
3. dp ?
use max increasing starting from an index and memoize it ?
any number either contributes or not 

recurrence relation
dp[i] = dp[i-1] / 1+dp[i-1]


bisect.bisect_left returns the leftmost place in the sorted list to insert the given element.
bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.

"""
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # find the sub greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        return len(sub)
    

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
         sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)