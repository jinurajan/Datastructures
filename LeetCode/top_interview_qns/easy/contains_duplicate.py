"""
 Contains Duplicate

Solution
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        hash_set = {}
        for num in nums:
            if num not in hash_set:
                hash_set[num] = 1
            else:
                hash_set[num] += 1
            if hash_set[num] >= 2:
                return True
        return len(nums) != len(hash_set)


if __name__ == "__main__":
    print Solution().containsDuplicate([1,2,3,1])
    print Solution().containsDuplicate([3,1])