"""
Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105


Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List


class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        n = len(nums)
        first = 0
        last = n-1
        find_points = 2
        import pdb; pdb.set_trace()
        while first < n-2 and last > 0 and find_points:
            if nums[first] < nums[first+1]:
                first += 1
            else:
                find_points -= 1
            if nums[last] > nums[last-1]:
                last -= 1
            else:
                find_points -= 1
        if first == n-1 and last == 0 or (last-first <= 1 and nums[first] < nums[last]):
            return 0
        return last - first + 1


from collections import deque
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lenN, left, right = len(nums) - 1, -1, -1
        maxN, minN = nums[0], nums[lenN]
        for i in range(1, len(nums)):
            a, b = nums[i], nums[lenN - i]
            if a < maxN:
                right = i
            else:
                maxN = a
            if b > minN:
                left = i
            else:
                minN = b
        return max(0, left + right - lenN + 1)







#
nums = [2,6,4,8,10,9,15]
print(Solution().findUnsortedSubarray(nums) == 5)
nums = [0]
print(Solution().findUnsortedSubarray(nums) == 0)
#
nums = [1,2,3,4]
print(Solution().findUnsortedSubarray(nums) == 0)

nums = [4,3,2,1]
print(Solution().findUnsortedSubarray(nums) == 4)

nums = [1, 2]
print(Solution().findUnsortedSubarray(nums) == 0)

nums = [1, 2, 3]
print(Solution().findUnsortedSubarray(nums) == 0)

nums = [1, 2, 3, 5]
print(Solution().findUnsortedSubarray(nums) == 0)

nums = [1, 2, 3, 5, 7]
print(Solution().findUnsortedSubarray(nums) == 0)
#
nums = [1,2,3,4,6,8,7, 10, 12, 11, 13, 14, 15]
print(Solution().findUnsortedSubarray(nums)==5)

nums = [2,1]
print(Solution().findUnsortedSubarray(nums)==2)

nums = [3,2,1]
print(Solution().findUnsortedSubarray(nums)==3)
#
nums = [1,3,2,4,5]
print(Solution().findUnsortedSubarray(nums))
#
