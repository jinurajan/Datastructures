"""
Search for a Range

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""
from typing import List

class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def binary_search(nums, l, r, target, key_fn,val):
            if l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    return binary_search(nums, l, mid-1, target, key_fn, val)
                elif nums[mid] < target:
                    return binary_search(nums, mid+1, r, target, key_fn, val)
                else:
                    if nums[mid] == target:
                        if key_fn == min:
                            val[0] = key_fn(mid, val[0])
                            return binary_search(nums, l, mid-1, target, key_fn, val)
                        else:
                            val[0] = key_fn(mid, val[0])
                            return binary_search(nums, mid + 1, r, target, key_fn, val)
            return val
        n = len(nums)
        left = [n]
        right = [-1]
        binary_search(nums, 0, len(nums)-1, target, min, left)
        if left[0] == n:
            return [-1, -1]
        binary_search(nums, 0, len(nums)-1, target, max, right)
        return [left[0], right[0]]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        l, r = 0, n-1
        left = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    left = mid
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, n-1
        right = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    right = mid
                l = mid+1
            else:
                r = mid - 1
        return [left, right]


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        l, r = 0, n-1
        right = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    right = mid
                l = mid+1
            else:
                r = mid - 1
        if right == -1:
            return [-1, -1]
        left = right
        i = right - 1
        while i >= 0:
            if nums[i] !=  target:
                return [left, right]
            left = i
            i -= 1
        return [left, right]




# print(Solution().searchRange([1,2,3,8,8,8,9,10, 12], 8))
# print(Solution().searchRange([1,2,3,8,8,8,9,10, 12], 1))
# print(Solution().searchRange([1,2,3,8,8,8,9,10, 12], 12))
# print(Solution().searchRange([1,2,3,8,8,8,9,10, 12], 13))

# print(Solution1().searchRange([1,2,3,8,8,8,9,10, 12], 8))
# print(Solution1().searchRange([1,2,3,8,8,8,9,10, 12], 1))
# print(Solution1().searchRange([1,2,3,8,8,8,9,10, 12], 12))
# print(Solution1().searchRange([1,2,3,8,8,8,9,10, 12], 13))

print(Solution2().searchRange([1,2,3,8,8,8,9,10, 12], 8))
print(Solution2().searchRange([1,2,3,8,8,8,9,10, 12], 1))
print(Solution2().searchRange([1,2,3,8,8,8,9,10, 12], 12))
print(Solution2().searchRange([1,2,3,8,8,8,9,10, 12], 13))


