"""
Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        nums_sum = sum(nums)
        if nums_sum & 1 == 1:
            # check if odd number
            return False
        result = 1
        for num in nums:
            result = result | (result << num)
        half = nums_sum >> 1
        return (result >> half) & 1 == 1



class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        sum_val = sum(nums)
        if sum_val % 2 == 1:
            return False
        n = len(nums)
        s = int(sum_val / 2)
        dp = [[False for i in range(s + 1)] for j in range(n)]
        for i in range(n):
            dp[i][0] = True
        for j in range(s + 1):
            dp[0][j] = nums[0] == j
        for i in range(1, n):
            for j in range(1, s + 1):
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]
        return dp[-1][-1]

nums = [1,2, 3, 4]
print(Solution().canPartition(nums))