"""
Third Maximum Number

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        sort_nums = sorted(set(nums), reverse=True)
        if len(sort_nums) < 3:
            return sort_nums[0]
        return sort_nums[2]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        def helper(nums):
            a, b, c = float("-inf"), float("-inf"), float("-inf")
            for num in nums:
                if num > a:
                    a, b, c = num, a, b
                elif num > b:
                    b, c = num,b
                elif num > c:
                    c = num
            return c

        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        elif len(nums) < 3:
            return max(nums)
        else:
            return helper(nums)




nums = [3,2,1]
print(Solution().thirdMax(nums))

nums = [1,2]
print(Solution().thirdMax(nums))

nums = [2,2,3,1]
print(Solution().thirdMax(nums))


