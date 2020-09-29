"""
Search in Rotated Sorted Array

Solution
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""
import bisect

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[-1]:
                r = m-1
            else:
                l = m + 1

        def binary_search(nums, l, r, key):
            if l <= r:
                mid = (l + r) / 2
                if nums[mid] == key:
                    return mid
                elif nums[mid] > key:
                    return binary_search(nums, l, mid - 1, key)
                else:
                    return binary_search(nums, mid + 1, r, key)
            return -1

        if target >= nums[0] and l != 0:
            res = bisect.bisect_left(nums[:l], target)
        else:
            res = bisect.bisect_left(nums[l:], target) + l
        return res if 0 <= res < n and nums[res] == target else -1



            


print Solution().search([4,5,6,7,0,1,2], 0)
print Solution().search([4,5,6,7,0,1,2], 3)
print Solution().search([4,5,6,7,0,1,2], 4)
print Solution().search([4,5,6,7,0,1,2], 2)