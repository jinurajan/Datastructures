"""
Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""
class Solution1(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(map(self.even_num_of_digits, nums))
    
    def even_num_of_digits(self, num):
        no = 0
        while num > 0:
            no += 1
            num = num / 10
        return 1 if no % 2 == 0 else 0

class Solution2(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len([x for x in nums if len(str(x)) % 2 == 0])


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenDigitCount = 0
        for i in range(len(nums)):
            if 10 ** 1 <= nums[i] and nums[i] < 10 ** 2:
                evenDigitCount += 1         
            elif (10 ** 3) <= nums[i] and nums[i] < (10 ** 4):
                evenDigitCount += 1
            elif (10 ** 5) == nums[i]:
                evenDigitCount += 1
        return evenDigitCount


print(Solution().findNumbers([555,901,482,1771]))
