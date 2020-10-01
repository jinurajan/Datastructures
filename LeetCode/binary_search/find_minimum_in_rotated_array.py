"""
Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        if nums[-1] < nums[-2]:
            return nums[-1]

        def binary_search(nums, l, r):
            if l <= r:
                mid = (l + r) // 2
                if nums[mid + 1] < nums[mid]:
                    return nums[mid + 1]
                if nums[mid] > nums[0]:
                    return binary_search(nums, mid+1, r)
                else:
                    return binary_search(nums, l, mid)

        return binary_search(nums, 0, n-1)


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        if nums[-1] < nums[-2]:
            return nums[-1]
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if mid + 1 <= n and nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            if nums[mid] > nums[0]:
                # lies in the biggest array part in rotated
                l = mid + 1
            else:
                r = mid



class Solution2:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
        return nums[l]


# print(Solution().findMin([4,5,6,7,-1,1,2]))
# print(Solution().findMin([4,5,-2,1,2,3]))
# print(Solution().findMin([4,5,6,7,8,0,1]))
# print(Solution().findMin([1, 2]))
# print(Solution().findMin([2, 1]))
print(Solution().findMin([3, 2, 1, 0]))

print("******")
# print(Solution1().findMin([4,5,6,7,-1,1,2]))
# print(Solution1().findMin([4,5,-2,1,2,3]))
# print(Solution1().findMin([4,5,6,7,8,0,1]))
# print(Solution1().findMin([1, 2]))
# print(Solution1().findMin([2, 1]))
print(Solution1().findMin([3, 2, 1, 0]))


print(Solution2().findMin([3, 2, 1, 0]))

