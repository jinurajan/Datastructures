"""
Squares of a Sorted Array


Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""
from typing import List


class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x * x for x in nums])


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) -1
        res = []
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res.insert(0, nums[l] ** 2)
                l += 1
            else:
                res.insert(0, nums[r] ** 2)
                r -= 1
        return res






nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))
