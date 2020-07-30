"""
  Two Sum

Solution
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_set = {}
        for i in range(len(nums)):
            print target - nums[i]
            if target-nums[i] in diff_set:
                return [diff_set[target-nums[i]], i]
            diff_set[nums[i]] = i
            print diff_set

if __name__ == "__main__":
    print Solution().twoSum([3,2,4], 6)
    # print Solution().twoSum([2,7,11,15], 9)