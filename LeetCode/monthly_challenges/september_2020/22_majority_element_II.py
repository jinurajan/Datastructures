"""
Given an integer array of size n, find all elements that appear more than n / 3 times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
from math import ceil

class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        hash_set = {}
        result = []
        l = int(ceil(n/3))
        for num in nums:
            if num in hash_set:
                hash_set[num] += 1
            else:
                hash_set[num] = 1
        for num, count in hash_set.items():
            if count > l:
                result.append(num)
        return result


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = [num for num in nums if nums.count(num) > int(n/3)]
        print nums
        return list(set(nums))


print Solution().majorityElement([1,1,1,3,3,2,2,2])
print Solution1().majorityElement([1,1,1,3,3,2,2,2])


