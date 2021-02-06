"""
Given an array nums of integers, return how many of them contain an even number of digits.

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.


Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.

1 <= nums.length <= 500
1 <= nums[i] <= 10^5

"""
from typing import List
from math import log10


class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
        def count_digits(num):
            digits = 0
            while num:
                num = num // 10
                digits += 1
            return digits

        counters = [count_digits(num) for num in nums]
        return sum(map(lambda x: 1 if x % 2 == 0 else 0, counters))

class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda x: 1 if len(str(x)) % 2 == 0 else 0, nums))


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([int(log10(num)) % 2 for num in nums])



nums = [555,901,482,1771]
print(Solution().findNumbers(nums))

nums = [12,345,2,6,7896]
print(Solution().findNumbers(nums))

nums = []
print(Solution().findNumbers(nums))
